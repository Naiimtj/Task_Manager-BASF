from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_todos():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hi!! Check '/docs' to see routes."

