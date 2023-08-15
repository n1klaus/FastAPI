#!/usr/bin/python3

from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship
from db.base import BaseClass

class User(BaseClass):
    """User Class"""
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    blogs = relationship('Blog', back_populates='author')
