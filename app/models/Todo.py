from db.base import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)


class CreateUpdateTodo(BaseModel):
    title: str
    description: str
    completed: bool
