from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_service_message() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API работает"}


def test_tasks_returns_typed_task_collection() -> None:
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "Первая задача"}]
