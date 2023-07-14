#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSION_LOCAL = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db() -> Generator:
    """"""
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()
