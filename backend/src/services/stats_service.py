from collections import defaultdict

from src.repositories.expense_repository import ExpenseRepository
from src.schemas.stats import CategoryStat, MonthlyStat, SummaryStats


class StatsService:
    def __init__(self, repository: ExpenseRepository):
        self._repo = repository

    def get_summary(self) -> dict:
        """Calculate overall summary statistics."""
        expenses = self._repo.get_all()
        settings = self._repo.get_settings()
        currency = settings.get("currency", "USD")

        total_count = len(expenses)
        if total_count == 0:
            return SummaryStats(
                total_amount=0.0,
                total_count=0,
                average_amount=0.0,
                highest_expense=None,
                lowest_expense=None,
                top_category=None,
                currency=currency
            ).model_dump()

        total_amount = sum(e.get("amount", 0.0) for e in expenses)
        average_amount = total_amount / total_count

        highest_expense = max(expenses, key=lambda x: x.get("amount", 0.0))
        lowest_expense = min(expenses, key=lambda x: x.get("amount", 0.0))

        cat_totals = defaultdict(float)
        for e in expenses:
            cat_totals[e.get("category")] += e.get("amount", 0.0)

        top_category = max(cat_totals.items(), key=lambda x: x[1])[0] if cat_totals else None

        return SummaryStats(
            total_amount=total_amount,
            total_count=total_count,
            average_amount=average_amount,
            highest_expense=highest_expense,
            lowest_expense=lowest_expense,
            top_category=top_category,
            currency=currency
        ).model_dump()

    def get_monthly_stats(self) -> list[dict]:
        """Calculate per-month totals for charting. Return sorted by month."""
        expenses = self._repo.get_all()
        monthly = defaultdict(lambda: {"total": 0.0, "count": 0})

        for e in expenses:
            month = e.get("date")[:7]  # YYYY-MM
            monthly[month]["total"] += e.get("amount", 0.0)
            monthly[month]["count"] += 1

        result = [
            MonthlyStat(month=month, total=data["total"], count=data["count"]).model_dump()
            for month, data in monthly.items()
        ]

        result.sort(key=lambda x: x["month"])
        return result

    def get_category_stats(self) -> list[dict]:
        """Calculate per-category breakdown."""
        expenses = self._repo.get_all()
        total_amount = sum(e.get("amount", 0.0) for e in expenses)

        cat_stats = defaultdict(lambda: {"total": 0.0, "count": 0})
        for e in expenses:
            cat_stats[e.get("category")]["total"] += e.get("amount", 0.0)
            cat_stats[e.get("category")]["count"] += 1

        result = []
        for cat, data in cat_stats.items():
            percentage = (data["total"] / total_amount * 100) if total_amount > 0 else 0
            average = data["total"] / data["count"] if data["count"] > 0 else 0
            result.append(
                CategoryStat(
                    category=cat,
                    total=data["total"],
                    count=data["count"],
                    percentage=percentage,
                    average=average
                ).model_dump()
            )

        result.sort(key=lambda x: x["total"], reverse=True)
        return result
