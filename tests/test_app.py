from app import create_app
from app.db import get_db_connection
from app.db import init_db


def test_health_check():
    init_db()  # Ensure the database is initialized before running the test
    app = create_app()
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_database_connection():
    connection = get_db_connection()
    

    assert connection.is_connected()

    connection.close()


def test_create_and_read_task():
    init_db()  # Ensure the database is initialized before running the test
    app = create_app()
    client = app.test_client()

    create_response = client.post(
        "/api/tasks",
        json={"title": "Test Docker CI"}
    )

    assert create_response.status_code == 201

    task_id = create_response.json["id"]

    get_response = client.get(f"/api/tasks/{task_id}")

    assert get_response.status_code == 200
    assert get_response.json["title"] == "Test Docker CI"