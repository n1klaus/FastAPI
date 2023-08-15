#!/usr/bin/python3

from typing import Any
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

@as_declarative()
class BaseClass:
    """Base Class"""
    id: Any
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """Generates table name from class name"""
        return cls.__name__.lower() + "s"