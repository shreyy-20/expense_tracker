"""Expense repository unit tests."""
import pytest
from pathlib import Path
from src.storage.json_file_manager import JsonFileManager
from src.repositories.expense_repository import ExpenseRepository
from src.models.expense import Expense
import uuid

@pytest.fixture
def repo(tmp_path):
    fm = JsonFileManager(tmp_path / "test_expenses.json")
    fm.ensure_file_exists()
    return ExpenseRepository(fm)

class TestExpenseRepository:
    def test_create_and_get_all(self, repo):
        exp = Expense(
            id=str(uuid.uuid4()),
            title="Test",
            amount=10.0,
            category="Food & Dining",
            date="2024-07-15"
        )
        repo.create(exp)
        all_exp = repo.get_all()
        assert len(all_exp) == 1
        assert all_exp[0]["title"] == "Test"
        
    def test_get_by_id(self, repo):
        exp_id = str(uuid.uuid4())
        exp = Expense(
            id=exp_id, title="Test", amount=10.0, category="Food & Dining", date="2024-07-15"
        )
        repo.create(exp)
        fetched = repo.get_by_id(exp_id)
        assert fetched is not None
        assert fetched["id"] == exp_id
        
        assert repo.get_by_id("nonexistent") is None
        
    def test_update(self, repo):
        exp_id = str(uuid.uuid4())
        exp = Expense(
            id=exp_id, title="Test", amount=10.0, category="Food & Dining", date="2024-07-15"
        )
        repo.create(exp)
        
        repo.update(exp_id, {"title": "Updated", "amount": 20.0})
        
        fetched = repo.get_by_id(exp_id)
        assert fetched["title"] == "Updated"
        assert fetched["amount"] == 20.0
        
    def test_delete(self, repo):
        exp_id = str(uuid.uuid4())
        exp = Expense(
            id=exp_id, title="Test", amount=10.0, category="Food & Dining", date="2024-07-15"
        )
        repo.create(exp)
        assert repo.delete(exp_id) is True
        assert repo.get_by_id(exp_id) is None
        assert repo.delete("nonexistent") is False
        
    def test_filtered_by_category(self, repo):
        exp1 = Expense(id=str(uuid.uuid4()), title="T1", amount=10.0, category="Utilities", date="2024-07-15")
        exp2 = Expense(id=str(uuid.uuid4()), title="T2", amount=10.0, category="Food & Dining", date="2024-07-15")
        repo.create(exp1)
        repo.create(exp2)
        
        result = repo.get_filtered(category="Utilities")
        assert len(result) == 1
        assert result[0]["title"] == "T1"
        
    def test_sorted_by_amount(self, repo):
        exp1 = Expense(id=str(uuid.uuid4()), title="T1", amount=50.0, category="Utilities", date="2024-07-15")
        exp2 = Expense(id=str(uuid.uuid4()), title="T2", amount=10.0, category="Food & Dining", date="2024-07-15")
        repo.create(exp1)
        repo.create(exp2)
        
        result = repo.get_filtered(sort_by="amount", sort_order="asc")
        assert result[0]["amount"] == 10.0
        assert result[1]["amount"] == 50.0
        
    def test_categories_crud(self, repo):
        categories = repo.get_categories()
        assert "Food & Dining" in categories
        
        repo.add_category("New Category")
        categories = repo.get_categories()
        assert "New Category" in categories
