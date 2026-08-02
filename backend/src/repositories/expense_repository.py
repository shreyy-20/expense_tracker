from src.core.constants import ALLOWED_SORT_FIELDS, DEFAULT_SORT_FIELD
from src.models.expense import Expense
from src.storage.json_file_manager import JsonFileManager


class ExpenseRepository:
    def __init__(self, file_manager: JsonFileManager):
        self._fm = file_manager

    def get_all(self) -> list[dict]:
        """Return all expenses as dicts."""
        data = self._fm.read_data()
        return data.get("expenses", [])

    def get_by_id(self, expense_id: str) -> dict | None:
        """Return expense dict by ID, or None."""
        expenses = self.get_all()
        for e in expenses:
            if e.get("id") == expense_id:
                return e
        return None

    def create(self, expense: Expense) -> dict:
        """Add expense to storage, return the created expense dict."""
        data = self._fm.read_data()
        expense_dict = expense.to_dict()
        data.setdefault("expenses", []).append(expense_dict)
        self._fm.write_data(data)
        return expense_dict

    def update(self, expense_id: str, updates: dict) -> dict | None:
        """Update expense by ID. Return updated dict or None if not found."""
        data = self._fm.read_data()
        expenses = data.get("expenses", [])
        for i, e in enumerate(expenses):
            if e.get("id") == expense_id:
                expense_obj = Expense.from_dict(e)
                expense_obj.update(**updates)
                updated_dict = expense_obj.to_dict()
                expenses[i] = updated_dict
                self._fm.write_data(data)
                return updated_dict
        return None

    def delete(self, expense_id: str) -> bool:
        """Delete expense by ID. Return True if deleted, False if not found."""
        data = self._fm.read_data()
        expenses = data.get("expenses", [])
        new_expenses = [e for e in expenses if e.get("id") != expense_id]
        if len(new_expenses) == len(expenses):
            return False
        data["expenses"] = new_expenses
        self._fm.write_data(data)
        return True

    def delete_many(self, expense_ids: list[str]) -> int:
        """Delete multiple expenses. Return count deleted."""
        data = self._fm.read_data()
        expenses = data.get("expenses", [])
        ids_set = set(expense_ids)
        new_expenses = [e for e in expenses if e.get("id") not in ids_set]
        deleted_count = len(expenses) - len(new_expenses)
        if deleted_count > 0:
            data["expenses"] = new_expenses
            self._fm.write_data(data)
        return deleted_count

    def get_filtered(
        self,
        category: str | None = None,
        search: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        amount_min: float | None = None,
        amount_max: float | None = None,
        sort_by: str = "date",
        sort_order: str = "desc",
    ) -> list[dict]:
        """Return filtered and sorted expenses."""
        expenses = self.get_all()
        filtered = []

        for e in expenses:
            if category and e.get("category") != category:
                continue
            if search and search.lower() not in e.get("title", "").lower():
                continue
            if date_from and e.get("date") < date_from:
                continue
            if date_to and e.get("date") > date_to:
                continue
            if amount_min is not None and e.get("amount", 0.0) < amount_min:
                continue
            if amount_max is not None and e.get("amount", 0.0) > amount_max:
                continue
            filtered.append(e)

        sort_field = sort_by if sort_by in ALLOWED_SORT_FIELDS else DEFAULT_SORT_FIELD
        reverse = (sort_order == "desc")

        # Sort handle numeric vs string gracefully if needed, but dict items are fine
        filtered.sort(key=lambda x: x.get(sort_field), reverse=reverse)
        return filtered

    def get_categories(self) -> list[str]:
        """Return current category list."""
        data = self._fm.read_data()
        return data.get("categories", [])

    def add_category(self, category: str) -> list[str]:
        """Add a custom category. Return updated list."""
        data = self._fm.read_data()
        categories = data.get("categories", [])
        if category not in categories:
            categories.append(category)
            data["categories"] = categories
            self._fm.write_data(data)
        return categories

    def remove_category(self, category: str) -> list[str]:
        """Remove a category. Return updated list."""
        data = self._fm.read_data()
        categories = data.get("categories", [])
        if category in categories:
            categories.remove(category)
            data["categories"] = categories
            self._fm.write_data(data)
        return categories

    def get_settings(self) -> dict:
        """Return current settings dict."""
        data = self._fm.read_data()
        return data.get("settings", {})

    def update_settings(self, updates: dict) -> dict:
        """Update settings. Return updated settings dict."""
        data = self._fm.read_data()
        settings = data.get("settings", {})
        settings.update(updates)
        data["settings"] = settings
        self._fm.write_data(data)
        return settings
