"""Statistics API endpoint tests."""
import pytest

pytestmark = pytest.mark.asyncio

class TestSummaryStats:
    async def test_summary_empty(self, client):
        response = await client.get("/api/v1/stats/summary")
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["total_amount"] == 0
        assert data["total_count"] == 0

    async def test_summary_with_data(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
        response = await client.get("/api/v1/stats/summary")
        data = response.json()["data"]
        assert data["total_count"] == 5
        expected_total = sum(e["amount"] for e in sample_expenses)
        assert abs(data["total_amount"] - expected_total) < 0.01

class TestMonthlyStats:
    async def test_monthly_empty(self, client):
        response = await client.get("/api/v1/stats/monthly")
        assert response.json()["data"] == []

    async def test_monthly_with_data(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
        response = await client.get("/api/v1/stats/monthly")
        data = response.json()["data"]
        assert len(data) > 0
        assert "month" in data[0]
        assert "total" in data[0]
        assert "count" in data[0]

class TestCategoryStats:
    async def test_category_empty(self, client):
        response = await client.get("/api/v1/stats/categories")
        assert response.json()["data"] == []

    async def test_category_with_data(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
        response = await client.get("/api/v1/stats/categories")
        data = response.json()["data"]

        food = next((c for c in data if c["category"] == "Food & Dining"), None)
        assert food is not None
        assert food["count"] == 2

        total_pct = sum(c["percentage"] for c in data)
        assert abs(total_pct - 100.0) < 0.1
