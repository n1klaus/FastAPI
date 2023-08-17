#!/usr/bin/python3

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.blog import BlogCreate, BlogView
from db.repository.blog import create_new_blog, retrieve_blog

router = APIRouter()

@router.post("/blogs", reponse_model=BlogView, status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    """Creates and returns the newly created blog"""
    blog = create_new_blog(blog-blog, db=db, author_id=1)
    return blog

@router.get("blogs/{id}", response_model=BlogView)
def get_blog(id: int, db: Session = Depends(get_db)):
    """Returns an existing blog with the given id"""
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with ID {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return blog
