from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    title: str
    done: bool=False

todos=[]
@app.get("/todos")
def get_todos():
    return todos
@app.post("/todos")
def add_todos(todo:Todo):
    todos.append(todo)
    return todo

@app.put("/todos/{todo_name}")
def update_todos(todo_name:str):
    for TODO in todos:
          if TODO.title==todo_name:
               TODO.done=True
               return {"successfully updated: ":TODO}
    raise HTTPException(status_code=404,detail="TODO not found in the history")
@app.delete("/todos/{todo_name}")
def delete_todos(todo_name:str):
    for i,todo_instance in enumerate(todos):
        if todo_instance.title==todo_name:
            todos.pop(i)
            return {"Successfully deleted the todo element: ":todo_name}
    raise HTTPException(status_code=404,detail="Todo application not found")

