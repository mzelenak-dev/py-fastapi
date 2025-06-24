from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "This is my first FastAPI"}

@app.post("/items/")
async def create_item(item: Item):
  item_dict = item.dict()
  if item.tax:
    price_with_tax = item.price + item.tax
    item_dict.update({
      "price_with_tax": price_with_tax
    })
    return item_dict

@app.get("/items/{num}")
async def read_num(num: int):
  return {"number": num}

@app.get("/items/{item_id}")
async def read_item(item_id):
  return {"item_id": item_id}

@app.get("/users/me")
async def read_current_user():
  return {"user": "this is the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
  return {"user_id": user_id}