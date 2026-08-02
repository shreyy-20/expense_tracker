"""Statistics response schemas."""
from pydantic import BaseModel


class SummaryStats(BaseModel):
    """Overall expense summary."""
    total_amount: float
    total_count: int
    average_amount: float
    highest_expense: dict | None = None  # {title, amount, date}
    lowest_expense: dict | None = None
    top_category: str | None = None
    currency: str = "USD"

class CategoryStat(BaseModel):
    """Per-category statistics."""
    category: str
    total: float
    count: int
    percentage: float
    average: float

class MonthlyStat(BaseModel):
    """Per-month statistics for charting."""
    month: str  # YYYY-MM format
    total: float
    count: int
