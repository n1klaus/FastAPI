#!/usr/bin/python3
""""""
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.config import get_settings
from core.hashing import Hasher
from core.security import create_access_token
from db.repository.login import get_user
from db.session import get_db
from schemas.token import Token

settings = get_settings()
router = APIRouter()


def authenticate_user(email: str, password: str, db: Session):
    """"""
    user = get_user(email=email, db=db)
    if not user or not Hasher.verify(password, user.password):
        return False
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """"""
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            detail="Incorrect username or password",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
