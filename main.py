from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# =========================
# Hello World GET request
# =========================

@app.get("/")
async def root():
    return {"message": "Hello World"}


# =========================
# GET request w/ parameter
# =========================

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# =========================
# POST request
# =========================


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/itempost/")
async def create_item(item: Item):
    return item
