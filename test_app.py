import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the root route for correct HTTP response and content."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
