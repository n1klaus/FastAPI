#!/usr/bin/python3

""""""

from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.repository.login import get_user
from db.session import get_db
from core.config import get_settings

settings = get_settings()

auth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def create_access_token(data: dict, expires_delta: Optional[timedelta]=None):
    """"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(auth2_scheme), db: Session = Depends(get_db)):
    """"""
    Credentials_Exception = HTTPException(detail="Could not validate credentials", status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise Credentials_Exception
    except JWTError:
        raise Credentials_Exception
    user = get_user(email=email, db=db)
    if user is None:
        raise Credentials_Exception
    return user