#!/usr/bin/python3

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    """Schema for creating a new User"""
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserView(BaseModel):
    """Schema for viewing an existing User"""
    id: int
    email: EmailStr
    is_active: bool

    class Config():
        """Converts obj to json"""
        orm_mode = True
