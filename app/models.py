# app/models.py
from pydantic import BaseModel  # type: ignore


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    on_offer: bool
