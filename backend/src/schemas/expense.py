"""Expense request and response schemas."""
from datetime import date
from pydantic import BaseModel, Field, field_validator
from src.core.constants import MIN_TITLE_LENGTH, MAX_TITLE_LENGTH, MIN_AMOUNT, MAX_AMOUNT

class ExpenseCreate(BaseModel):
    """Schema for creating a new expense."""
    title: str = Field(..., min_length=MIN_TITLE_LENGTH, max_length=MAX_TITLE_LENGTH, description="Expense title")
    amount: float = Field(..., gt=0, le=MAX_AMOUNT, description="Expense amount")
    category: str = Field(..., min_length=1, description="Expense category")
    date: str = Field(..., description="Expense date in YYYY-MM-DD format")
    
    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        v = v.strip()
        if len(v) < MIN_TITLE_LENGTH:
            raise ValueError("Title cannot be empty or whitespace only")
        return v
    
    @field_validator("amount")
    @classmethod
    def validate_amount(cls, v: float) -> float:
        return round(v, 2)
    
    @field_validator("date")
    @classmethod
    def validate_date(cls, v: str) -> str:
        try:
            date.fromisoformat(v)
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        return v

class ExpenseUpdate(ExpenseCreate):
    """Schema for full update (PUT) - all fields required."""
    pass

class ExpensePartialUpdate(BaseModel):
    """Schema for partial update (PATCH) - all fields optional."""
    title: str | None = Field(None, min_length=MIN_TITLE_LENGTH, max_length=MAX_TITLE_LENGTH)
    amount: float | None = Field(None, gt=0, le=MAX_AMOUNT)
    category: str | None = Field(None, min_length=1)
    date: str | None = None
    
    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str | None) -> str | None:
        if v is not None:
            v = v.strip()
            if len(v) < MIN_TITLE_LENGTH:
                raise ValueError("Title cannot be empty or whitespace only")
        return v
    
    @field_validator("amount")
    @classmethod
    def validate_amount(cls, v: float | None) -> float | None:
        if v is not None:
            return round(v, 2)
        return v
    
    @field_validator("date")
    @classmethod
    def validate_date(cls, v: str | None) -> str | None:
        if v is not None:
            try:
                date.fromisoformat(v)
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")
        return v

class ExpenseResponse(BaseModel):
    """Schema for expense in API responses."""
    id: str
    title: str
    amount: float
    category: str
    date: str
    created_at: str
    updated_at: str

class ExpenseQueryParams(BaseModel):
    """Schema for query parameters when listing expenses."""
    page: int = Field(default=1, ge=1)
    per_page: int = Field(default=20, ge=1, le=100)
    category: str | None = None
    search: str | None = None
    sort_by: str = Field(default="date")
    sort_order: str = Field(default="desc")
    date_from: str | None = None
    date_to: str | None = None
    amount_min: float | None = Field(None, ge=0)
    amount_max: float | None = None

class BulkDeleteRequest(BaseModel):
    """Schema for bulk delete."""
    ids: list[str] = Field(..., min_length=1, max_length=100, description="List of expense IDs to delete")

class ImportExpenseItem(BaseModel):
    """Schema for a single imported expense."""
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1)
    date: str
    
    @field_validator("date")
    @classmethod
    def validate_date(cls, v: str) -> str:
        try:
            date.fromisoformat(v)
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        return v

class ImportRequest(BaseModel):
    """Schema for import request."""
    expenses: list[ImportExpenseItem] = Field(..., min_length=1, max_length=1000)
