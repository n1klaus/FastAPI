#!/usr/bin/python3

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    """Schema for creating a new User"""
    email: EmailStr
    password: str = Field(..., min_length=8)
