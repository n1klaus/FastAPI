#!/usr/bin/python3

from sqlalchemy.orm import Session
from schemas.blog import BlogCreate
from db.models.blog import Blog

def create_new_blog(blog: BlogCreate, db: Session, author_id: int = 1):
    """Creates a new blog"""
    blog = Blog(**blog.dict(), author_id = author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retrieve_blog(id: int, db: Session):
    """Retrieves an existing blog"""
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def list_blogs(db: Session):
    """Retrives all existing blogs"""
    blogs = db.query(Blog).filter(Blog.is_active==True).all()
    return blogs
