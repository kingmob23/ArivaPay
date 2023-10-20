import pytest
from ..app import app


@pytest.fixture
def client():
    return app.test_client()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Main Page" in response.data


def test_account_page(client):
    response = client.get("/account")
    assert response.status_code == 200
    assert b"Personal" in response.data
