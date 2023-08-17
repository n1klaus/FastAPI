#!/usr/bin/python3
""""""
from sqlalchemy.orm import Session

from db.repository.user import create_new_user
from schemas.user import UserCreate


def create_test_user(db: Session):
    """"""
    user = UserCreate(email="ping@fastapitutorial.com", password="Hello!101")
    user = create_new_user(user, db=db)
    return user
