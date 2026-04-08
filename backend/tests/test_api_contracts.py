from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ingestion_api():
    payload = {"file_data": "base64", "mime_type": "image/jpeg", "source_type": "business_card"}
    response = client.post("/api/v1/ingest/document", json=payload)
    assert response.status_code == 202
    assert "task_id" in response.json()


def test_enrichment_api():
    payload = {"lead_id": "test-uuid"}
    response = client.post("/api/v1/enrich", json=payload)
    assert response.status_code == 200
    assert "score" in response.json()


def test_generation_api():
    payload = {"lead_id": "test-uuid", "prompt_template_id": "test-template"}
    response = client.post("/api/v1/generate-draft", json=payload)
    assert response.status_code == 200
    assert "draft_id" in response.json()


def test_delivery_api():
    payload = {"draft_id": "test-uuid"}
    response = client.post("/api/v1/delivery/send", json=payload)
    assert response.status_code == 202
    assert "interaction_log_id" in response.json()
