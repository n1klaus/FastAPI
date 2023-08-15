#!/usr/bin/python3

import os
from pydantic import BaseSettings
from functools import lru_cache
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('.env'))

class Settings(BaseSettings):
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT : int =  int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DB : str = os.getenv("POSTGRES_DB")


@lru_cache
def get_settings():
    return Settings()

