# app/crud.py
import json
from models import Item

DATA_FILE = "data/items.json"
ID_FILE = "data/next_id.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_data(items):
    with open(DATA_FILE, "w") as f:
        json.dump(items, f, indent=2)


def load_next_id():
    try:
        with open(ID_FILE, "r") as f:
            return json.load(f)["next_id"]
    except FileNotFoundError:
        return 1
    except json.JSONDecodeError:
        return 1


def save_next_id(next_id):
    with open(ID_FILE, "w") as f:
        json.dump({"next_id": next_id}, f, indent=2)


def get_items():
    return load_data()


def get_item(item_id: int):
    items = load_data()
    for item in items:
        if item['id'] == item_id:
            return item
    return None


def create_item(item: Item):
    items = load_data()
    items.append(item.dict())
    save_data(items)
    return item


def update_item(item_id: int, updated_item: Item):
    items = load_data()
    for index, item in enumerate(items):
        if item['id'] == item_id:
            items[index] = updated_item.dict()
            save_data(items)
            return updated_item
    return None


def delete_item(item_id: int):
    items = load_data()
    for index, item in enumerate(items):
        if item['id'] == item_id:
            del items[index]
            save_data(items)
            return True
    return False
