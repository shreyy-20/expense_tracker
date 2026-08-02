"""Statistics API endpoints."""
from fastapi import APIRouter, Depends
from src.services.stats_service import StatsService
from src.dependencies import get_stats_service

router = APIRouter(prefix="/stats", tags=["Statistics"])

@router.get("/summary", summary="Get expense summary statistics")
async def get_summary(service: StatsService = Depends(get_stats_service)):
    summary = service.get_summary()
    return {"status": "success", "data": summary}

@router.get("/monthly", summary="Get monthly expense totals")
async def get_monthly(service: StatsService = Depends(get_stats_service)):
    monthly = service.get_monthly_stats()
    return {"status": "success", "data": monthly}

@router.get("/categories", summary="Get category breakdown")
async def get_categories(service: StatsService = Depends(get_stats_service)):
    categories = service.get_category_stats()
    return {"status": "success", "data": categories}
