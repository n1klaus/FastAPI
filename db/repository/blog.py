#!/usr/bin/python3

from sqlalchemy.orm import Session
from schemas.blog import BlogCreate, BlogUpdate
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

def update_blog(id: int, blog: BlogUpdate, author_id: int, db: Session):
    """"""
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return {"error":f"Blog with id {id} does not exist"}
    if not blog_in_db.author_id == author_id:
        return {"error":f"Only the author can modify the blog"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db

def delete_blog(id: int, author_id: int, db: Session):
    """"""
    blog_in_db = db.query(Blog).filter(Blog.id == id)
    if not blog_in_db.first():
        return {"error": "Could not find blog with given id {id}"}
    if not blog_in_db.first().author_id == author_id:             #new
        return {"error":f"Only the author can delete a blog"}
    blog_in_db.delete()
    db.commit()
    return {"msg": f"Successfully deleted blog with id {id}"}
