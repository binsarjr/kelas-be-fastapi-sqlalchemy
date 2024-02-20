from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
from app.models.Todo import Todo

DATABASE_URL = "postgresql://postgres:postgres@localhost/sqlalchemy"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
