"""Health and version endpoint tests."""
import pytest

pytestmark = pytest.mark.asyncio

class TestHealth:
    async def test_health_check(self, client):
        response = await client.get("/api/v1/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "uptime_seconds" in data
        assert data["storage"] == "ok"

class TestVersion:
    async def test_version(self, client):
        response = await client.get("/api/v1/version")
        assert response.status_code == 200
        data = response.json()
        assert "version" in data
        assert "name" in data
