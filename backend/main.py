from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
fruits = []

# Pydantic model for fruit data
class Fruit(BaseModel):
    name: str
    color: str = None
    price: float = None

@app.get("/")
def main():
    return {"hello": "world"}

@app.post("/add-fruit")
def adding_fruit(fruit: Fruit):
    fruits.append(fruit.dict())
    return {"message": "Fruit added successfully", "fruit": fruit}

@app.get("/fruits")
def get_fruits():
    return {"fruits": fruits}

@app.get("/fruits/{fruit_name}")
def get_fruit(fruit_name: str):
    for fruit in fruits:
        if fruit["name"].lower() == fruit_name.lower():
            return {"fruit": fruit}
    return {"error": "Fruit not found"}

@app.delete("/fruits/{fruit_name}")
def delete_fruit(fruit_name: str):
    for i, fruit in enumerate(fruits):
        if fruit["name"].lower() == fruit_name.lower():
            deleted_fruit = fruits.pop(i)
            return {"message": "Fruit deleted", "fruit": deleted_fruit}
    return {"error": "Fruit not found"}