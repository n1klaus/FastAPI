#!/usr/bin/python3

from sqlalchemy.orm import Session
from schemas.blog import BlogCreate
from db.models.blog import Blog

def create_new_blog(blog: BlogCreate, db: Session, author_id: int = 1):
    blog = Blog(**blog.dict(), author_id = author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog
