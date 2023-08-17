#!/usr/bin/python3

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    """Class to handle passwords"""

    @staticmethod
    def verify(plain_password, hashed_password):
        """Verifies provided plain password string with hashed password"""
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def get_password_hash(plain_password):
        """Returns hashed form of the plain password from the string"""
        return pwd_context.hash(secret=plain_password)
