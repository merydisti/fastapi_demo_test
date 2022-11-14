from tests.test_routes.utils.before_insert import before_insert_sample
from fastapi.testclient import TestClient


def test_sample_insert(client: TestClient):
    # ARRANGE
    item = {
        "name": "Sample 1",
        "description": "Sample description 1"
    }

    # ACT
    response = client.post('/item', json=item)

    # ASSERT
    assert response.status_code == 201
    assert response.json()["success"] == True
    assert response.json()["item"]["name"] == "Sample 1"

def test_sample_get_one(client: TestClient):
    # ARRANGE
    before_insert_sample()

    # ACT
    response = client.get('/item/1')

    # ASSERT
    assert response.status_code == 200
    assert response.json()["success"] == True
    assert response.json()["item"]["id"] == 1
    assert response.json()["item"]["name"] == "Sample 1"

def test_sample_get_one_not_exists(client: TestClient):
    # ACT
    response = client.get('/item/1')

    # ASSERT
    assert response.status_code == 404
    assert response.json()["success"] == False

def test_sample_get_all(client: TestClient):
    # ARRANGE
    before_insert_sample()
    before_insert_sample(name="Sample 2", description="Sample description 2")

    # ACT
    response = client.get('/item')

    # ASSERT
    assert response.status_code == 200
    assert response.json()["success"] == True
    assert response.json()["items"][0]["id"] == 1
    assert response.json()["items"][0]["name"] == "Sample 1"
    assert len(response.json()["items"]) == 2
