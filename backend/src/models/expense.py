"""Expense domain model."""
from datetime import date, datetime, timezone
from uuid import uuid4

class Expense:
    """Domain model representing an expense."""
    
    def __init__(
        self,
        title: str,
        amount: float,
        category: str,
        date: str,  # ISO format YYYY-MM-DD
        id: str | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
    ):
        self.id = id or str(uuid4())
        self.title = title.strip()
        self.amount = round(float(amount), 2)
        self.category = category
        self.date = date
        self.created_at = created_at or datetime.now(timezone.utc).isoformat()
        self.updated_at = updated_at or datetime.now(timezone.utc).isoformat()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            id=data.get("id"),
            title=data["title"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
    
    def update(self, **kwargs) -> None:
        """Update expense fields. Only updates provided fields."""
        for key, value in kwargs.items():
            if value is not None and hasattr(self, key):
                if key == "title":
                    value = value.strip()
                elif key == "amount":
                    value = round(float(value), 2)
                setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc).isoformat()
