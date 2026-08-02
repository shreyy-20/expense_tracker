"""Statistics API endpoints."""

from typing import Annotated

from fastapi import APIRouter, Depends

from src.dependencies import get_stats_service
from src.services.stats_service import StatsService

router = APIRouter(prefix="/stats", tags=["Statistics"])
StatsServiceDep = Annotated[StatsService, Depends(get_stats_service)]


@router.get("/summary", summary="Get expense summary statistics")
async def get_summary(service: StatsServiceDep) -> dict:
    summary = service.get_summary()
    return {"status": "success", "data": summary}


@router.get("/monthly", summary="Get monthly expense totals")
async def get_monthly(service: StatsServiceDep) -> dict:
    monthly = service.get_monthly_stats()
    return {"status": "success", "data": monthly}


@router.get("/categories", summary="Get category breakdown")
async def get_categories(service: StatsServiceDep) -> dict:
    categories = service.get_category_stats()
    return {"status": "success", "data": categories}
