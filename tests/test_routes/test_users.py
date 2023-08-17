#!/usr/bin/python3
""""""
from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    """"""
    data = {"email": "testuser@nofoobar.com", "password": "testing101"}
    response = client.post("/", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True
