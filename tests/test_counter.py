"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""

import pytest

from src.counter import app
from src import status


@pytest.fixture()
def client():
  return app.test_client()

@pytest.mark.usefixtures("client")
class TestCounterEndPoints:
    def test_create_a_counter(self, client):
        result = client.post('/counters/foo')
        assert result.status_code == status.HTTP_201_CREATED


    def test_duplicate_a_counter(self, client):
        result = client.post('/counters/bar')
        assert result.status_code == status.HTTP_201_CREATED
        result = client.post('/counters/bar')
        assert result.status_code == status.HTTP_409_CONFLICT

    def test_update_a_counter(self, client):
        result = client.post('/counters/upd')
        assert result.status_code == status.HTTP_201_CREATED
        result = client.post('counters/upd/update')
        assert result.status_code == status.HTTP_200_OK

    def test_delete_a_counter(self, client):
        result = client.post('/counters/dde')
        assert result.status_code == status.HTTP_201_CREATED
        result = client.post('counters/dde/delete')
        assert result.status_code == status.HTTP_204_NO_CONTENT
