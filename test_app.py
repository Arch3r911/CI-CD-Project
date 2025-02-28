import pytest
import requests

BASE_URL = 'http://localhost:5000'

def test_create_user():
    response = requests.post(f'{BASE_URL}/create_user', json={"name": "John"})
    assert response.status_code == 200
    assert "User John created successfully!" in response.text
