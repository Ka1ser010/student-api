
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

TEST_DATABASE_URL = "sqlite:///./students_test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def setup_module():
    Base.metadata.create_all(bind=engine)


def teardown_module():
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("students_test.db"):
        os.remove("students_test.db")


def test_create_student():
    response = client.post(
        "/students/",
        json={
            "full_name": "Maria Silva",
            "email": "mary@example.com",
            "phone": "31999999999",
            "level": "Starter",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["full_name"] == "Mary Jane"
    assert "id" in data


def test_create_student_duplicate_email_fails():
    client.post(
        "/students/",
        json={"full_name": "Ana", "email": "duplicaded@example.com", "level": "starter"},
    )
    response = client.post(
        "/students/",
        json={"full_name": "Outra Ana", "email": "duplicado@example.com", "level": "iniciante"},
    )
    assert response.status_code == 400


def test_list_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_student_not_found():
    response = client.get("/students/9999")
    assert response.status_code == 404


def test_update_student():
    create_response = client.post(
        "/students/",
        json={"full_name": "Carlos", "email": "carlos@example.com", "level": "iniciante"},
    )
    student_id = create_response.json()["id"]

    update_response = client.put(
        f"/students/{student_id}", json={"level": "intermediario"}
    )
    assert update_response.status_code == 200
    assert update_response.json()["level"] == "intermediario"


def test_delete_student():
    create_response = client.post(
        "/students/",
        json={"full_name": "Delete", "email": "delete@example.com", "level": "starter"},
    )
    student_id = create_response.json()["id"]

    delete_response = client.delete(f"/students/{student_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 404
