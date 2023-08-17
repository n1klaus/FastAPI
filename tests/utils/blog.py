#!/usr/bin/python3

""""""

from sqlalchemy.orm import Session
from db.repository.blog import create_new_blog
from schemas.blog import BlogCreate
from tests.utils.user import create_test_user

def create_test_blog(db: Session):
    """"""
    blog = BlogCreate(title="first_blog", content="Tests make the system stable!")
    user = create_test_user(db=db)
    blog = create_new_blog(blog=blog, db=db, author_id=user.id)
    return blog
