#!/usr/bin/python3

from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

@as_declarative()
class Base:
    """Base Class"""
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """Generates table name from class name"""
        return cls.__name__.lower()