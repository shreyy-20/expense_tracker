"""Expense service unit tests."""
import pytest
from pathlib import Path
from src.storage.json_file_manager import JsonFileManager
from src.repositories.expense_repository import ExpenseRepository
from src.services.expense_service import ExpenseService
from src.schemas.expense import ExpenseCreate, ExpenseQueryParams
from src.core.exceptions import NotFoundException, ValidationException

@pytest.fixture
def service(tmp_path):
    fm = JsonFileManager(tmp_path / "test_expenses.json")
    fm.ensure_file_exists()
    repo = ExpenseRepository(fm)
    return ExpenseService(repo)

class TestExpenseService:
    def test_create_and_get(self, service):
        expense_data = ExpenseCreate(
            title="Test",
            amount=10.0,
            category="Food & Dining",
            date="2024-07-15"
        )
        created = service.create_expense(expense_data)
        assert created["id"] is not None
        assert created["title"] == "Test"
        
        fetched = service.get_expense(created["id"])
        assert fetched["id"] == created["id"]
        
    def test_create_invalid_category(self, service):
        expense_data = ExpenseCreate(
            title="Test",
            amount=10.0,
            category="NonExistent",
            date="2024-07-15"
        )
        with pytest.raises(ValidationException):
            service.create_expense(expense_data)
            
    def test_delete_nonexistent(self, service):
        with pytest.raises(NotFoundException):
            service.delete_expense("nonexistent-id")
            
    def test_list_with_pagination(self, service):
        for i in range(5):
            service.create_expense(ExpenseCreate(
                title=f"Test {i}", amount=10.0, category="Food & Dining", date="2024-07-15"
            ))
            
        params = ExpenseQueryParams(page=1, per_page=2)
        result, pagination = service.list_expenses(params)
        assert len(result) == 2
        assert pagination.total_items == 5
        assert pagination.has_next is True
        
    def test_add_custom_category(self, service):
        service.add_category("My Custom Category")
        categories = service.get_categories()
        assert "My Custom Category" in categories
