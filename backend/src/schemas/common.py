"""Common schemas used across the application."""
from pydantic import BaseModel, Field
from src.core.constants import DEFAULT_PAGE, DEFAULT_PER_PAGE, MAX_PER_PAGE

class PaginationParams(BaseModel):
    page: int = Field(default=DEFAULT_PAGE, ge=1, description="Page number")
    per_page: int = Field(default=DEFAULT_PER_PAGE, ge=1, le=MAX_PER_PAGE, description="Items per page")

class PaginationMeta(BaseModel):
    page: int
    per_page: int
    total_items: int
    total_pages: int
    has_next: bool
    has_prev: bool

class ErrorDetail(BaseModel):
    field: str | None = None
    message: str
    type: str = "validation_error"

class ErrorResponse(BaseModel):
    status: str = "error"
    error: dict  # {code, message, details[]}
    request_id: str | None = None

class SuccessResponse(BaseModel):
    status: str = "success"
    data: dict | list | None = None
    pagination: PaginationMeta | None = None
    message: str | None = None
