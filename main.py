#!/usr/bin/python3
from fastapi import FastAPI

from api.base import api_router
from core.config import get_settings
from db.base import BaseClass as Base
from db.session import engine

settings = get_settings()


def create_tables():
    """Create all tables needed by the application"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def include_routers(app: FastAPI):
    app.include_router(api_router)


def start_app():
    """Start the FastAPI application"""
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_routers(app)
    return app


app = start_app()


@app.get("/")
def hello_api():
    return {"msg": "Hello FastAPI🚀"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug"
    )
