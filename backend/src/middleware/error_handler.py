"""Global exception handler middleware."""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from src.core.exceptions import AppException
from src.utils.logger import logger

def setup_error_handlers(app: FastAPI) -> None:
    
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
        request_id = getattr(request.state, "request_id", None)
        error_dict = {
            "code": exc.error_code,
            "message": exc.message,
        }
        if hasattr(exc, "details") and exc.details:
            error_dict["details"] = exc.details
            
        content = {
            "status": "error",
            "error": error_dict
        }
        if request_id:
            content["request_id"] = request_id
            
        return JSONResponse(status_code=exc.status_code, content=content)
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        request_id = getattr(request.state, "request_id", None)
        details = []
        for error in exc.errors():
            field = ".".join([str(loc) for loc in error.get("loc", [])])
            details.append({
                "field": field,
                "message": error.get("msg"),
                "type": error.get("type")
            })
            
        content = {
            "status": "error",
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Validation failed",
                "details": details
            }
        }
        if request_id:
            content["request_id"] = request_id
            
        return JSONResponse(status_code=422, content=content)
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        request_id = getattr(request.state, "request_id", None)
        logger.error(f"Unhandled Exception: {str(exc)}")
        
        content = {
            "status": "error",
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "An unexpected error occurred."
            }
        }
        if request_id:
            content["request_id"] = request_id
            
        return JSONResponse(status_code=500, content=content)
