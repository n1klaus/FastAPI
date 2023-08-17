#!/usr/bin/python3
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import get_settings

settings = get_settings()
SQLALCHEMY_DATABASE_URL: str = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
    settings.POSTGRES_USER,
    settings.POSTGRES_PASSWORD,
    settings.POSTGRES_SERVER,
    settings.POSTGRES_PORT,
    settings.POSTGRES_DB,
)

print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSION_LOCAL = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db() -> Generator:
    """Creats a database session"""
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()
