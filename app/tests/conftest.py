from app.config import config
from fastapi import FastAPI
from fastapi.testclient import TestClient
from typing import Generator
from .mock_requests import *
from unittest import mock
from typing import Any
import pytest


def start_application():
    app = config()
    test_client = TestClient(app)
    return test_client

@pytest.fixture(scope="function")
def client() -> Generator[FastAPI, Any, None]:
   
    with \
    mock.patch('requests.get', side_effect=mock_requests_get), \
    mock.patch('requests.post', side_effect=mock_requests_post), \
    mock.patch('requests.request', side_effect=mock_requests_request):
        _app = start_application()
        yield _app

