#!/usr/bin/python3

from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date

class BlogCreate(BaseModel):
    """Schema for creating a blog"""
    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = values.get('title').replace(" ", "-").lower()
        return values
    
class BlogView(BaseModel):
    title: str
    content: Optional[str]
    created_at: date

    class Config():
        orm_mode = True
