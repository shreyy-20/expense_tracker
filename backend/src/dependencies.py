"""Dependency injection for FastAPI."""
from functools import lru_cache

from src.core.config import get_settings
from src.repositories.expense_repository import ExpenseRepository
from src.services.expense_service import ExpenseService
from src.services.stats_service import StatsService
from src.storage.json_file_manager import JsonFileManager


@lru_cache
def get_file_manager() -> JsonFileManager:
    settings = get_settings()
    fm = JsonFileManager(settings.data_file_path)
    fm.ensure_file_exists()
    return fm

def get_expense_repository() -> ExpenseRepository:
    return ExpenseRepository(get_file_manager())

def get_expense_service() -> ExpenseService:
    return ExpenseService(get_expense_repository())

def get_stats_service() -> StatsService:
    return StatsService(get_expense_repository())
