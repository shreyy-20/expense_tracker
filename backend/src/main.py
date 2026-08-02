"""FastAPI application factory."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from src.core.config import get_settings
from src.core.constants import API_V1_PREFIX
from src.api.router import api_router
from src.middleware.cors import setup_cors
from src.middleware.error_handler import setup_error_handlers
from src.middleware.request_id import RequestIDMiddleware
from src.middleware.security_headers import SecurityHeadersMiddleware
from src.dependencies import get_file_manager
from src.utils.logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    settings = get_settings()
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    logger.info(f"Environment: {settings.environment}")
    fm = get_file_manager()  # This ensures the data file exists
    logger.info(f"Data file: {settings.data_file_path}")
    yield
    # Shutdown
    logger.info("Shutting down...")

def create_app() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="A production-ready expense tracking API with beautiful analytics.",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )
    
    # Rate limiting
    limiter = Limiter(key_func=get_remote_address, default_limits=[settings.rate_limit])
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    
    # Middleware (order matters - last added = first executed)
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(RequestIDMiddleware)
    setup_cors(app)
    
    # Error handlers
    setup_error_handlers(app)
    
    # Routes
    app.include_router(api_router, prefix=API_V1_PREFIX)
    
    return app

app = create_app()
