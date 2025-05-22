import pytest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to API of Product's Recomendatinos"}


def test_create_user() -> None:
    response = client.post("/users/", params={"name": "Bat Test"})
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["id"] == 1
    assert user_data["name"] == "Bat Test"


def test_list_users() -> None:
    response = client.get('/users/')
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_product():
    response = client.post('/products/', json={
        "name": "Prod A",
        "category": "Cat 01",
        "tags": ["tagZ5", "tagZ6"],
    },)
    assert response.status_code == 200
    assert response.json()["name"] == "Prod A"
    assert response.json()["category"] == "Cat 01"
    assert response.json()["tags"] == ["tagZ5", "tagZ6"]


def test_list_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_history():
    response = client.post("/purchase_history/1", json={"products_ids": [1]})
    assert response.status_code == 200
    assert response.json() == {"message": "Purchase history updated!!"}


def test_recommendations():
    response = client.post(
        "/recommendations/1", json={"categories": ["Cat 01"], "tags": ["tagZ5"]}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
