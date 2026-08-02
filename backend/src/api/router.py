"""API router aggregation."""
from fastapi import APIRouter

from src.api.v1.expenses import router as expenses_router
from src.api.v1.health import router as health_router
from src.api.v1.stats import router as stats_router

api_router = APIRouter()
api_router.include_router(expenses_router)
api_router.include_router(stats_router)
api_router.include_router(health_router)
