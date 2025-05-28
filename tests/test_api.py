import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_map_preview():
    response = client.post("/map-preview", json={
        "input": {
            "user": {
                "name": "Tom",
                "age": 30
            }
        },
        "mappings": [
            {"key": "username", "type": "jsonpath", "source": "$.user.name"},
            {"key": "ageGroup", "type": "cel", "transform": "input.user.age > 18 ? 'adult' : 'minor'"}
        ]
    })

    assert response.status_code == 200
    assert response.json() == {
        "output": {
            "username": "Tom",
            "ageGroup": "adult"
        },
        "errors": []
    }