#!/usr/bin/python3
from datetime import date
from typing import Optional

from pydantic import root_validator
from sqlmodel import SQLModel


class BlogCreate(SQLModel):
    """Schema for creating a blog"""

    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class BlogView(SQLModel):
    """Schema for viewing a blog"""

    id: int
    title: str
    content: Optional[str]
    created_at: date
    updated_at: date


class BlogUpdate(BlogCreate):
    """Schema for updating a blog"""

    ...
