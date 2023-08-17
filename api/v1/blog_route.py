#!/usr/bin/python3
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from core.security import get_current_user
from db.models.user import User
from db.repository.blog import create_new_blog
from db.repository.blog import delete_blog
from db.repository.blog import list_blogs
from db.repository.blog import retrieve_blog
from db.repository.blog import update_blog
from db.session import get_db
from schemas.blog import BlogCreate
from schemas.blog import BlogUpdate
from schemas.blog import BlogView

router = APIRouter()


@router.post("/blogs", response_model=BlogView, status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    """Creates and returns the newly created blog"""
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/blogs/{id}", response_model=BlogView)
def get_blog(id: int, db: Session = Depends(get_db)):
    """Returns an existing blog with the given id"""
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.get("/blogs", response_model=List[BlogView])
def get_all_blogs(db: Session = Depends(get_db)):
    """Returns a list if all blogs"""
    blogs = list_blogs(db=db)
    return blogs


@router.put("/blogs/{id}", response_model=BlogView)
def update_a_blog(
    id: int,
    blog: BlogUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """"""
    blog = update_blog(id=id, blog=blog, author_id=current_user.id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.delete("/blogs/{id}")
def delete_a_blog(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """"""
    message = delete_blog(id=id, author_id=current_user.id, db=db)
    if "error" in message:
        raise HTTPException(
            detail=message["error"], status_code=status.HTTP_404_NOT_FOUND
        )
    return {"msg": f"Successfully deleted blog with id {id}"}
