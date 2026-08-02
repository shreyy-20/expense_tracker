"""Expense API endpoint tests."""
import pytest

pytestmark = pytest.mark.asyncio

class TestCreateExpense:
    async def test_create_valid_expense(self, client, sample_expense):
        response = await client.post("/api/v1/expenses", json=sample_expense)
        assert response.status_code == 201
        data = response.json()
        assert data["status"] == "success"
        assert data["data"]["title"] == "Morning Coffee"
        assert data["data"]["amount"] == 4.50
        assert "id" in data["data"]
        assert "created_at" in data["data"]
    
    async def test_create_with_negative_amount(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": -10, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
    
    async def test_create_with_zero_amount(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 0, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
    
    async def test_create_with_empty_title(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "   ", "amount": 10, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 422
    
    async def test_create_with_invalid_date(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 10, "category": "Food & Dining", "date": "not-a-date"
        })
        assert response.status_code == 422
    
    async def test_create_with_invalid_category(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Test", "amount": 10, "category": "NonExistentCategory", "date": "2024-07-15"
        })
        assert response.status_code == 422
    
    async def test_create_strips_whitespace_title(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "  Coffee  ", "amount": 10, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 201
        assert response.json()["data"]["title"] == "Coffee"
    
    async def test_create_rounds_amount(self, client):
        response = await client.post("/api/v1/expenses", json={
            "title": "Coffee", "amount": 4.999, "category": "Food & Dining", "date": "2024-07-15"
        })
        assert response.status_code == 201
        assert response.json()["data"]["amount"] == 5.0

class TestGetExpenses:
    async def test_list_empty(self, client):
        response = await client.get("/api/v1/expenses")
        assert response.status_code == 200
        data = response.json()
        assert data["data"] == []
        assert data["pagination"]["total_items"] == 0
    
    async def test_list_with_data(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
        response = await client.get("/api/v1/expenses")
        assert response.status_code == 200
        assert response.json()["pagination"]["total_items"] == 5
    
    async def test_filter_by_category(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
        response = await client.get("/api/v1/expenses?category=Food+%26+Dining")
        data = response.json()
        assert all(e["category"] == "Food & Dining" for e in data["data"])
        assert len(data["data"]) == 2
    
    async def test_search(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
        response = await client.get("/api/v1/expenses?search=coffee")
        data = response.json()
        assert len(data["data"]) == 1
        assert data["data"][0]["title"] == "Coffee"
    
    async def test_sort_by_amount(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
        response = await client.get("/api/v1/expenses?sort_by=amount&sort_order=desc")
        amounts = [e["amount"] for e in response.json()["data"]]
        assert amounts == sorted(amounts, reverse=True)
    
    async def test_pagination(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
        response = await client.get("/api/v1/expenses?page=1&per_page=2")
        data = response.json()
        assert len(data["data"]) == 2
        assert data["pagination"]["has_next"] is True

class TestGetExpenseById:
    async def test_get_existing(self, client, sample_expense):
        create_resp = await client.post("/api/v1/expenses", json=sample_expense)
        exp_id = create_resp.json()["data"]["id"]
        response = await client.get(f"/api/v1/expenses/{exp_id}")
        assert response.status_code == 200
        assert response.json()["data"]["id"] == exp_id
    
    async def test_get_nonexistent(self, client):
        response = await client.get("/api/v1/expenses/nonexistent-id")
        assert response.status_code == 404

class TestUpdateExpense:
    async def test_put_update(self, client, sample_expense):
        create_resp = await client.post("/api/v1/expenses", json=sample_expense)
        exp_id = create_resp.json()["data"]["id"]
        update_data = {
            "title": "Updated Coffee",
            "amount": 5.50,
            "category": "Food & Dining",
            "date": "2024-07-16"
        }
        response = await client.put(f"/api/v1/expenses/{exp_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["title"] == "Updated Coffee"
        assert data["amount"] == 5.50
    
    async def test_patch_partial_update(self, client, sample_expense):
        create_resp = await client.post("/api/v1/expenses", json=sample_expense)
        exp_id = create_resp.json()["data"]["id"]
        response = await client.patch(f"/api/v1/expenses/{exp_id}", json={"title": "New Title"})
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["title"] == "New Title"
        assert data["amount"] == sample_expense["amount"]
    
    async def test_update_nonexistent(self, client, sample_expense):
        response = await client.put("/api/v1/expenses/nonexistent", json=sample_expense)
        assert response.status_code == 404

class TestDeleteExpense:
    async def test_delete_existing(self, client, sample_expense):
        create_resp = await client.post("/api/v1/expenses", json=sample_expense)
        exp_id = create_resp.json()["data"]["id"]
        response = await client.delete(f"/api/v1/expenses/{exp_id}")
        assert response.status_code == 204
    
    async def test_delete_nonexistent(self, client):
        response = await client.delete("/api/v1/expenses/nonexistent")
        assert response.status_code == 404
    
    async def test_delete_then_get(self, client, sample_expense):
        create_resp = await client.post("/api/v1/expenses", json=sample_expense)
        exp_id = create_resp.json()["data"]["id"]
        await client.delete(f"/api/v1/expenses/{exp_id}")
        response = await client.get(f"/api/v1/expenses/{exp_id}")
        assert response.status_code == 404
    
    async def test_bulk_delete(self, client, sample_expenses):
        ids = []
        for exp in sample_expenses:
            resp = await client.post("/api/v1/expenses", json=exp)
            ids.append(resp.json()["data"]["id"])
        
        response = await client.request("DELETE", "/api/v1/expenses", json={"ids": ids[:2]})
        assert response.status_code == 204
        
        list_resp = await client.get("/api/v1/expenses")
        assert list_resp.json()["pagination"]["total_items"] == 3

class TestExportImport:
    async def test_export_empty(self, client):
        response = await client.post("/api/v1/expenses/export")
        assert response.status_code == 200
        assert response.json()["data"] == []
    
    async def test_import_expenses(self, client):
        import_data = {"expenses": [
            {"title": "Imported Coffee", "amount": 5.0, "category": "Food & Dining", "date": "2024-01-01"},
            {"title": "Imported Uber", "amount": 12.0, "category": "Transportation", "date": "2024-01-02"},
        ]}
        response = await client.post("/api/v1/expenses/import", json=import_data)
        assert response.status_code == 201
        
        list_response = await client.get("/api/v1/expenses")
        assert list_response.json()["pagination"]["total_items"] == 2
    
    async def test_export_import_roundtrip(self, client, sample_expenses):
        for exp in sample_expenses:
            await client.post("/api/v1/expenses", json=exp)
            
        export_resp = await client.post("/api/v1/expenses/export")
        exported_data = export_resp.json()["data"]
        assert len(exported_data) == 5
        
        # In a real app we might delete them, but we can just import them again to test
        import_resp = await client.post("/api/v1/expenses/import", json={"expenses": exported_data})
        assert import_resp.status_code == 201
        assert import_resp.json()["data"]["imported"] == 5
