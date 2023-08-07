#!/usr/bin/python3

from fastapi import FastAPI
from db.session import engine
from db.base import Base
from core.config import settings
from api.base import api_router

def create_tables():
    """"""
    Base.metadata.create_all(bind=engine)

def include_routers(app: FastAPI):
    app.include_router(api_router)


def start_app():
    """"""
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_routers(app)
    return app

app = start_app()

@app.get('/')
def hello_api():
    return {'msg': 'Hello FastAPI🚀'}

