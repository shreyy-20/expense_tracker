"""Health and version endpoints."""
import time
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.core.config import get_settings
from src.dependencies import get_file_manager

router = APIRouter(tags=["System"])

_start_time = time.time()

@router.get("/health", summary="Health check")
async def health_check():
    fm = get_file_manager()
    storage_healthy = fm.is_healthy()
    settings = get_settings()
    uptime = round(time.time() - _start_time, 2)
    status_val = "healthy" if storage_healthy else "unhealthy"
    status_code = 200 if storage_healthy else 503
    return JSONResponse(
        status_code=status_code,
        content={
            "status": status_val,
            "uptime_seconds": uptime,
            "storage": "ok" if storage_healthy else "error",
            "environment": settings.environment,
        }
    )

@router.get("/version", summary="App version")
async def version():
    settings = get_settings()
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }
