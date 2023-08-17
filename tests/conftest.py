#!/usr/bin/python3
""""""
import os
import sys
from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from db.base import BaseClass as Base
from db.session import get_db
from api.base import api_router


def start_app():
    """"""
    test_app = FastAPI()
    test_app.include_router(api_router)
    return test_app


DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """Creates a fresh database on each test case"""
    Base.metadata.create_all(engine)
    test_app = start_app()
    yield test_app
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def session(app: FastAPI) -> Generator[TestingSession, Any, None]:
    """"""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSession(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(app: FastAPI, session: TestingSession) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def get_test_db():
        """"""
        try:
            yield session
        finally:
            pass

    app.dependency_overrides[get_db] = get_test_db
    with TestClient(app=app) as test_client:
        yield test_client
