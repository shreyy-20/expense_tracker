"""Expense API endpoints."""
from fastapi import APIRouter, Depends, Query, status

from src.dependencies import get_expense_service
from src.schemas.expense import (
    BulkDeleteRequest,
    ExpenseCreate,
    ExpensePartialUpdate,
    ExpenseQueryParams,
    ExpenseUpdate,
    ImportRequest,
)
from src.services.expense_service import ExpenseService

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.get("", summary="List expenses")
async def list_expenses(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    category: str | None = Query(None),
    search: str | None = Query(None),
    sort_by: str = Query("date"),
    sort_order: str = Query("desc"),
    date_from: str | None = Query(None),
    date_to: str | None = Query(None),
    amount_min: float | None = Query(None, ge=0),
    amount_max: float | None = Query(None),
    service: ExpenseService = Depends(get_expense_service),
):
    params = ExpenseQueryParams(
        page=page, per_page=per_page, category=category, search=search,
        sort_by=sort_by, sort_order=sort_order, date_from=date_from,
        date_to=date_to, amount_min=amount_min, amount_max=amount_max
    )
    items, pagination = service.list_expenses(params)
    return {"status": "success", "data": items, "pagination": pagination.model_dump()}

@router.post("", status_code=status.HTTP_201_CREATED, summary="Create expense")
async def create_expense(data: ExpenseCreate, service: ExpenseService = Depends(get_expense_service)):
    expense = service.create_expense(data)
    return {"status": "success", "data": expense, "message": "Expense created successfully"}

@router.delete("", status_code=status.HTTP_204_NO_CONTENT, summary="Bulk delete expenses")
async def bulk_delete(data: BulkDeleteRequest, service: ExpenseService = Depends(get_expense_service)):
    service.bulk_delete_expenses(data.ids)
    return None

@router.post("/export", summary="Export expenses")
async def export_expenses(service: ExpenseService = Depends(get_expense_service)):
    expenses = service.export_expenses()
    return {"status": "success", "data": expenses}

@router.post("/import", status_code=status.HTTP_201_CREATED, summary="Import expenses")
async def import_expenses(data: ImportRequest, service: ExpenseService = Depends(get_expense_service)):
    result = service.import_expenses([e.model_dump() for e in data.expenses])
    return {"status": "success", "data": result, "message": "Import completed"}

# Category endpoints
@router.get("/categories/list", summary="Get categories")
async def get_categories(service: ExpenseService = Depends(get_expense_service)):
    categories = service.get_categories()
    return {"status": "success", "data": categories}

@router.post("/categories", status_code=status.HTTP_201_CREATED, summary="Add category")
async def add_category(data: dict, service: ExpenseService = Depends(get_expense_service)):
    name = data.get("name", "").strip()
    categories = service.add_category(name)
    return {"status": "success", "data": categories, "message": f"Category '{name}' added"}

@router.delete("/categories/{category_name}", summary="Remove category")
async def remove_category(category_name: str, service: ExpenseService = Depends(get_expense_service)):
    categories = service.remove_category(category_name)
    return {"status": "success", "data": categories, "message": "Category removed"}

# Settings endpoints
@router.get("/settings", summary="Get settings")
async def get_settings(service: ExpenseService = Depends(get_expense_service)):
    settings = service.get_settings()
    return {"status": "success", "data": settings}

@router.patch("/settings", summary="Update settings")
async def update_settings(data: dict, service: ExpenseService = Depends(get_expense_service)):
    settings = service.update_settings(data)
    return {"status": "success", "data": settings, "message": "Settings updated"}

# Expense ID endpoints (must be after specific paths like /export to avoid path parameter conflicts)
@router.get("/{expense_id}", summary="Get expense by ID")
async def get_expense(expense_id: str, service: ExpenseService = Depends(get_expense_service)):
    expense = service.get_expense(expense_id)
    return {"status": "success", "data": expense}

@router.put("/{expense_id}", summary="Update expense (full)")
async def update_expense(expense_id: str, data: ExpenseUpdate, service: ExpenseService = Depends(get_expense_service)):
    expense = service.update_expense(expense_id, data)
    return {"status": "success", "data": expense, "message": "Expense updated successfully"}

@router.patch("/{expense_id}", summary="Update expense (partial)")
async def partial_update_expense(expense_id: str, data: ExpensePartialUpdate, service: ExpenseService = Depends(get_expense_service)):
    expense = service.partial_update_expense(expense_id, data)
    return {"status": "success", "data": expense, "message": "Expense updated successfully"}

@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete expense")
async def delete_expense(expense_id: str, service: ExpenseService = Depends(get_expense_service)):
    service.delete_expense(expense_id)
    return None
