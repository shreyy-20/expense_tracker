"""Validation and edge case tests."""
import pytest

pytestmark = pytest.mark.asyncio

class TestAmountValidation:
    async def test_negative_amount(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": -50.0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_zero_amount(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_very_large_amount(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 1000000000.0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_amount_precision(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 10.12345, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 201
        assert response.json()["data"]["amount"] == 10.12

class TestTitleValidation:
    async def test_empty_title(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "", "amount": 10.0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_whitespace_only_title(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "   ", "amount": 10.0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_very_long_title(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "a" * 101, "amount": 10.0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_special_characters_in_title(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Café ☕", "amount": 10.0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 201
        assert response.json()["data"]["title"] == "Café ☕"

class TestDateValidation:
    async def test_invalid_date_format(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 10.0, "category": "Food & Dining", "date": "15/07/2024"
        })
        assert response.status_code == 422
        
    async def test_valid_date(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 10.0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 201

class TestCategoryValidation:
    async def test_invalid_category(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 10.0, "category": "Invalid", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_valid_category(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 10.0, "category": "Utilities", "date": "2024-07-15"
        })
        assert response.status_code == 201

class TestMissingFields:
    async def test_missing_title(self, client):
        response = await client.post("/api/v1/expenses", json={
            "amount": 10.0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_missing_amount(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
        
    async def test_missing_all_fields(self, client):
        response = await client.post("/api/v1/expenses", json={})
        assert response.status_code == 422
