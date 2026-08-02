import math

from src.core.constants import ALLOWED_SORT_FIELDS, MAX_CATEGORIES, MAX_TITLE_LENGTH
from src.core.exceptions import DuplicateError, NotFoundError, ValidationError
from src.models.expense import Expense
from src.repositories.expense_repository import ExpenseRepository
from src.schemas.common import PaginationMeta
from src.schemas.expense import (
    ExpenseCreate,
    ExpensePartialUpdate,
    ExpenseQueryParams,
    ExpenseUpdate,
)


class ExpenseService:
    def __init__(self, repository: ExpenseRepository):
        self._repo = repository

    def list_expenses(self, params: ExpenseQueryParams) -> tuple[list[dict], PaginationMeta]:
        """Get paginated, filtered expense list."""
        sort_by = params.sort_by if params.sort_by in ALLOWED_SORT_FIELDS else "date"

        filtered = self._repo.get_filtered(
            category=params.category,
            search=params.search,
            date_from=params.date_from,
            date_to=params.date_to,
            amount_min=params.amount_min,
            amount_max=params.amount_max,
            sort_by=sort_by,
            sort_order=params.sort_order,
        )

        total_items = len(filtered)
        total_pages = math.ceil(total_items / params.per_page) if total_items > 0 else 1
        page = params.page if params.page <= total_pages else total_pages
        page = max(1, page)

        start_idx = (page - 1) * params.per_page
        end_idx = start_idx + params.per_page

        page_items = filtered[start_idx:end_idx]

        pagination_meta = PaginationMeta(
            page=page,
            per_page=params.per_page,
            total_items=total_items,
            total_pages=total_pages,
            has_next=page < total_pages,
            has_prev=page > 1,
        )

        return page_items, pagination_meta

    def get_expense(self, expense_id: str) -> dict:
        """Get single expense. Raises NotFoundError."""
        expense = self._repo.get_by_id(expense_id)
        if not expense:
            raise NotFoundError("Expense", expense_id)
        return expense

    def create_expense(self, data: ExpenseCreate) -> dict:
        """Create new expense. Validates category exists."""
        categories = self._repo.get_categories()
        if data.category not in categories:
            raise ValidationError(
                "Invalid category", details=[{"field": "category", "message": "Category not found"}]
            )

        expense = Expense(
            title=data.title, amount=data.amount, category=data.category, date=data.date
        )

        return self._repo.create(expense)

    def update_expense(self, expense_id: str, data: ExpenseUpdate) -> dict:
        """Full update. All fields required. Validates category."""
        categories = self._repo.get_categories()
        if data.category not in categories:
            raise ValidationError(
                "Invalid category", details=[{"field": "category", "message": "Category not found"}]
            )

        updates = data.model_dump()
        updated = self._repo.update(expense_id, updates)
        if not updated:
            raise NotFoundError("Expense", expense_id)
        return updated

    def partial_update_expense(self, expense_id: str, data: ExpensePartialUpdate) -> dict:
        """Partial update. Only provided fields updated."""
        updates = data.model_dump(exclude_unset=True)
        if "category" in updates:
            categories = self._repo.get_categories()
            if updates["category"] not in categories:
                raise ValidationError(
                    "Invalid category",
                    details=[{"field": "category", "message": "Category not found"}],
                )

        updated = self._repo.update(expense_id, updates)
        if not updated:
            raise NotFoundError("Expense", expense_id)
        return updated

    def delete_expense(self, expense_id: str) -> None:
        """Delete expense. Raises NotFoundError."""
        if not self._repo.delete(expense_id):
            raise NotFoundError("Expense", expense_id)

    def bulk_delete_expenses(self, ids: list[str]) -> int:
        """Delete multiple. Return count deleted."""
        return self._repo.delete_many(ids)

    def export_expenses(self) -> list[dict]:
        """Return all expenses for export."""
        return self._repo.get_all()

    def import_expenses(self, expenses_data: list[dict]) -> dict:
        """Import expenses. Return {imported: int, skipped: int, errors: []}."""
        imported = 0
        skipped = 0
        errors = []

        categories = self._repo.get_categories()

        for idx, item in enumerate(expenses_data):
            try:
                title = item.get("title")
                amount = item.get("amount")
                category = item.get("category")
                date = item.get("date")
                if category not in categories:
                    skipped += 1
                    errors.append({"index": idx, "error": f"Invalid category: {category}"})
                    continue

                expense = Expense(
                    title=str(title or ""),
                    amount=float(amount or 0),
                    category=str(category or ""),
                    date=str(date or ""),
                )
                self._repo.create(expense)
                imported += 1
            except Exception as e:
                skipped += 1
                errors.append({"index": idx, "error": str(e)})

        return {"imported": imported, "skipped": skipped, "errors": errors}

    def get_categories(self) -> list[str]:
        return self._repo.get_categories()

    def add_category(self, name: str) -> list[str]:
        if not name or len(name) > MAX_TITLE_LENGTH:
            raise ValidationError("Invalid category name")
        categories = self._repo.get_categories()
        if name in categories:
            raise DuplicateError("Category already exists")
        if len(categories) >= MAX_CATEGORIES:
            raise ValidationError("Maximum categories reached")
        return self._repo.add_category(name)

    def remove_category(self, name: str) -> list[str]:
        categories = self._repo.get_categories()
        if name not in categories:
            raise NotFoundError("Category", name)

        expenses = self._repo.get_filtered(category=name)
        if expenses:
            raise ValidationError("Cannot remove category in use")

        return self._repo.remove_category(name)

    def get_settings(self) -> dict:
        return self._repo.get_settings()

    def update_settings(self, updates: dict) -> dict:
        return self._repo.update_settings(updates)
