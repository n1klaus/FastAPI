#!/usr/bin/python3

from typing import Optional
from pydantic import root_validator
from sqlmodel import SQLModel
from datetime import date

class BlogCreate(SQLModel):
    """Schema for creating a blog"""
    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = values.get('title').replace(" ", "-").lower()
        return values
    
class BlogView(SQLModel):
    title: str
    content: Optional[str]
    created_at: date
    updated_at: date
