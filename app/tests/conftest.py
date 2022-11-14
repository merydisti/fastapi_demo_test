from app.main import app
from fastapi.testclient import TestClient
from typing import Generator
from typing import Any
import pytest
from app.main import app
from app.db import database, metadata, engine
from httpx import AsyncClient
from asgi_lifespan import LifespanManager

#app = LifespanManager(app)

# attach db to state
app.state.database = database

# define event like in production
@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    metadata.drop_all(engine)
    if database_.is_connected:
        await database_.disconnect()


@pytest.fixture
async def client() -> Generator[AsyncClient,Any,None]:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as client:
            yield client
