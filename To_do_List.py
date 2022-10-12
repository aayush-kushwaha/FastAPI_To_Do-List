from http.client import HTTPException
from unicodedata import name
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):

    name: str
    due_date: str
    description: Optional[str] = None

app = FastAPI(title="Todo API")

# CRUD Operations API

store_todo = []

@app.get("/")
async def home():
    return {"Hello": "World"}

@app.post("/todo/")
async def create_todo(todo: Todo): # Here we are inheriting class Todo
    store_todo.append(todo)
    return todo

@app.get("/todo/{id}")
async def get_todo(id: int): 
    try:
        return store_todo[id]
    except:
        IndexError

@app.put("/todo/{id}")
async def update_todo(id: int, todo: Todo): #Inheriting Todo class
    store_todo[id] = todo
    return store_todo[id]

@app.delete("/todo/{id}")
async def delete_todo(id: int):
    obj = store_todo[id]
    store_todo.pop(id)
    return obj