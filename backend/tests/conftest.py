"""Shared test fixtures."""

import os
from unittest.mock import patch

import pytest
from httpx import ASGITransport, AsyncClient

# Set test environment BEFORE importing app
os.environ["BACKEND_ENVIRONMENT"] = "testing"
os.environ["BACKEND_LOG_LEVEL"] = "warning"


@pytest.fixture
def temp_data_dir(tmp_path):
    """Create a temporary data directory."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture
def app(temp_data_dir):
    """Create a fresh FastAPI app with isolated test storage."""
    from src.core.config import get_settings
    from src.dependencies import get_file_manager

    # Clear LRU caches
    get_settings.cache_clear()
    get_file_manager.cache_clear()

    # Patch the data_dir setting
    with patch.dict(os.environ, {"BACKEND_DATA_DIR": str(temp_data_dir)}):
        get_settings.cache_clear()
        get_file_manager.cache_clear()
        from src.main import create_app

        test_app = create_app()
        yield test_app
        get_settings.cache_clear()
        get_file_manager.cache_clear()


@pytest.fixture
async def client(app):
    """Async HTTP client for testing."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


@pytest.fixture
def sample_expense():
    """Sample valid expense data."""
    return {
        "title": "Morning Coffee",
        "amount": 4.50,
        "category": "Food & Dining",
        "date": "2024-07-15",
    }


@pytest.fixture
def sample_expenses():
    """Multiple sample expenses for testing."""
    return [
        {"title": "Coffee", "amount": 4.50, "category": "Food & Dining", "date": "2024-07-15"},
        {"title": "Uber", "amount": 15.00, "category": "Transportation", "date": "2024-07-14"},
        {"title": "Groceries", "amount": 85.50, "category": "Food & Dining", "date": "2024-07-13"},
        {"title": "Netflix", "amount": 15.99, "category": "Entertainment", "date": "2024-07-12"},
        {"title": "Electric Bill", "amount": 95.00, "category": "Utilities", "date": "2024-07-10"},
    ]
