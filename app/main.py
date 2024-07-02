# app/main.py
from fastapi import FastAPI, HTTPException  # type: ignore
from pydantic import BaseModel  # type: ignore
from typing import Dict, List
from crud import get_items, get_item, create_item, update_item, delete_item, load_next_id, save_next_id
from models import Item

app = FastAPI()

next_id = load_next_id()


class ItemIn(BaseModel):
    name: str
    description: str
    price: float
    on_offer: bool


class ItemOut(ItemIn):
    id: int


@app.get("/items/", response_model=List[ItemOut])
def read_items():
    return get_items()


@app.get("/items/{item_id}", response_model=ItemOut)
def read_item(item_id: int):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items/", response_model=ItemOut)
def create_item_endpoint(item: ItemIn):
    global next_id
    new_item = Item(id=next_id, **item.dict())
    create_item(new_item)
    next_id += 1
    save_next_id(next_id)
    return new_item


@app.put("/items/{item_id}", response_model=ItemOut)
def update_item_endpoint(item_id: int, item: ItemIn):
    existing_item = get_item(item_id)
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = Item(id=item_id, **item.dict())
    update_item(item_id, updated_item)
    return updated_item


@app.delete("/items/{item_id}", response_model=Dict[str, str])
def delete_item_endpoint(item_id: int):
    success = delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted successfully"}
