#!/usr/bin/python3

from fastapi import APIRouter

from api.v1 import user_route, blog_route

api_router = APIRouter()
api_router.include_router(user_route.router, prefix="", tags=["users"])
api_router.include_router(blog_route.router, prefix="", tags=["blogs"])
