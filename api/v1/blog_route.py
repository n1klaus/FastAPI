#!/usr/bin/python3

from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from schemas.blog import BlogCreate, BlogView
from db.repository.blog import create_new_blog

router = APIRouter()

@router.post("/blogs", reponse_model=BlogView, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: BlogCreate, db: Session = Depends(get_db))
    blog = create_new_blog(blog-blog, db=db, author_id=1)
    return blog
