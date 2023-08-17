#!/usr/bin/python3

""""""

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from core.hashing import Hasher

from schemas.token import Token
from db.repository.login import get_user
from core.security import create_access_token
from db.session import get_db
from core.config import get_settings

settings = get_settings()
router = APIRouter()


def authenticate_user(email: str, password: str, db: Session):
    """"""
    user = get_user(email=email, db=db)
    if not user or not Hasher.verify(password, user.password):
        return False
    return user

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """"""
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(detail="Incorrect username or password", status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

