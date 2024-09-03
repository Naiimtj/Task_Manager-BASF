from fastapi.testclient import TestClient
from main import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# Configuración de la base de datos de prueba
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Sobrescribir la dependencia get_db
def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hi!! Check '/docs' to see routes."

def test_create_task_group():
    response = client.post("/task-groups", json={"name": "Work 2"})
    response = client.post("/task-groups", json={"name": "Work"})
    assert response.status_code == 200
    assert response.json()["name"] == "Work"

def test_get_all_task_groups():
    response = client.get("/task-groups")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_create_task():
    task_group_id = client.get("/task-groups").json()[0]["id"]
    response = client.post("/tasks", json={
        "title": "Task 2",
        "description": "First task description",
        "completed": False,
        "priority": "Low",
        "labels": ["work", "urgent"],
        "group_id": task_group_id
    })
    response = client.post("/tasks", json={
        "title": "Task 1",
        "description": "First task description",
        "completed": False,
        "priority": "Low",
        "labels": ["work", "urgent"],
        "group_id": task_group_id
    })
     # Imprime el cuerpo de la respuesta para depuración
    assert response.status_code == 200
    assert response.json()["title"] == "Task 1"

def test_get_all_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_search_task_by_title():
    response = client.get("/tasks/search", params={"title": "Task 1"})
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) > 0
    assert tasks[0]["title"] == "Task 1"

def test_update_task():
    task_id = client.get("/tasks").json()[0]["id"]
    response = client.put(f"/tasks/{task_id}", json={
        "title": "Updated Task 1",
        "description": "Updated description",
        "completed": True
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task 1"
    assert response.json()["completed"] is True

def test_delete_task():
    task_id = client.get("/tasks").json()[0]["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted successfully"}

def test_delete_all_tasks():
    response = client.delete("/tasks")
    assert response.status_code == 200
    assert response.json() == {"message": "All tasks deleted successfully"}

def test_delete_task_group():
    task_group_id = client.get("/task-groups").json()[0]["id"]
    response = client.delete(f"/task-groups/{task_group_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Task Group deleted successfully"}

def test_delete_all_task_groups():
    response = client.delete("/task-groups")
    assert response.status_code == 200
    assert "All tasks groups deleted successfully" in response.json()["message"]
