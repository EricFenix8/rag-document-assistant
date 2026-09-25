from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "RAG Document Assistant API"
    }


def test_upload_invalid_file():
    response = client.post(
        "/documents",
        files={
            "file": (
                "test.txt",
                b"This is not a PDF.",
                "text/plain"
            )
        }
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Only PDF files are supported."
    }


def test_ask():

    with open("data/sample.pdf", "rb") as file:
        upload_response = client.post(
            "/documents",
            files={
                "file": (
                    "sample.pdf",
                    file,
                    "application/pdf"
                )
            }
        )

    assert upload_response.status_code == 200

    response = client.post(
        "/ask",
        json={
            "question": "What is this document about?",
            "top_k": 2
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "sources" in data

    assert len(data["sources"]) == 2

    assert all(
        "source" in source
        for source in data["sources"]
    )

    assert all(
        "page" in source
        for source in data["sources"]
    )

    assert all(
        "score" in source
        for source in data["sources"]
    )