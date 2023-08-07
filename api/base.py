#!/usr/bin/python3

from fastapi import APIRouter

from api.v1 import user_router

api_router = APIRouter()
api_router.include_router(user_router.router, prefix="", tags=["users"])