from app.tests.test_routes.utils.before_insert import before_insert_sample
from app.models.sample import Sample
import pytest

@pytest.mark.anyio
async def test_sample_insert(client):
    # ARRANGE
    item = {
        "name": "Sample 1",
        "description": "Sample description 1"
    }

    # ACT
    response = await client.post('/sample/', json=item)

    # ASSERT
    assert response.status_code == 201
    assert response.json()["name"] == "Sample 1"

@pytest.mark.anyio
async def test_sample_get_all(client):
    # ARRANGE
    await before_insert_sample()
    await before_insert_sample(name="Sample 2", description="Sample description 2")
    # ACT
    response = await client.get('/sample/')
    # ASSERT
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Sample 1"
    assert len(response.json()) == 2
    
