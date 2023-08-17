#!/usr/bin/python3
""""""
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from tests.utils.blog import create_test_blog


def test_create_blog(client: TestClient, session: Session):
    """"""
    blog = create_test_blog(db=session)
    response = client.get(f"/blogs/{blog.id}/")
    assert response.status_code == 200
    assert response.json()["title"] == blog.title
