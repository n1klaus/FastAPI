#!/usr/bin/python3
from pydantic import EmailStr
from sqlmodel import Field
from sqlmodel import SQLModel


class UserCreate(SQLModel):
    """Schema for creating a new User"""

    email: EmailStr
    password: str = Field(..., min_length=8)


class UserView(SQLModel):
    """Schema for viewing an existing User"""

    id: int
    email: EmailStr
    is_active: bool
