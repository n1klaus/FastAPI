#!/usr/bin/python3

from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base import BaseClass

class Blog(BaseClass):
    """Blog class"""
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='blogs')
    is_active = Column(Boolean, default=False)
