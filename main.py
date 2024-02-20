from typing import Union

from fastapi import FastAPI

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db.base import Base
from db.session import engine, SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.Todo import Todo, CreateUpdateTodo

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_all_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()


@app.post("/")
def create_todo(todo: CreateUpdateTodo, db: Session = Depends(get_db)):
    db.add(
        Todo(title=todo.title, description=todo.description, completed=todo.completed)
    )
    db.commit()
    return {"message": "Todo created successfully."}


@app.put("/{id}")
def update_todo(id: int, todo: CreateUpdateTodo, db: Session = Depends(get_db)):
    db.query(Todo).filter(Todo.id == id).update(jsonable_encoder(todo))
    db.commit()
    return db.query(Todo).filter(Todo.id == id).first()


@app.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    db.query(Todo).filter(Todo.id == id).delete()
    db.commit()
    return {"message": "Todo deleted successfully"}
