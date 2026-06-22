from unittest.mock import MagicMock, patch

# Mock all external services before importing app.main.
# At module level, app code instantiates SentenceTransformer and
# QdrantClient — both try to connect to external resources CI doesn't have.
with (
    patch("sentence_transformers.SentenceTransformer", return_value=MagicMock()),
    patch("qdrant_client.QdrantClient", return_value=MagicMock()),
):
    from fastapi.testclient import TestClient

    from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}