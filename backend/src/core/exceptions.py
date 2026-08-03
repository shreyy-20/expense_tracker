"""Custom exception classes for the application."""


class AppError(Exception):
    """Base application error."""

    def __init__(self, message: str, status_code: int = 500, error_code: str = "INTERNAL_ERROR"):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(self.message)


class NotFoundError(AppError):
    def __init__(self, resource: str = "Resource", resource_id: str = ""):
        message = (
            f"{resource} not found"
            if not resource_id
            else f"{resource} with id '{resource_id}' not found"
        )
        super().__init__(message=message, status_code=404, error_code="NOT_FOUND")


class ValidationError(AppError):
    def __init__(self, message: str, details: list[dict] | None = None):
        self.details = details or []
        super().__init__(message=message, status_code=422, error_code="VALIDATION_ERROR")


class DuplicateError(AppError):
    def __init__(self, message: str = "Resource already exists"):
        super().__init__(message=message, status_code=409, error_code="DUPLICATE")


class StorageError(AppError):
    def __init__(self, message: str = "Storage operation failed"):
        super().__init__(message=message, status_code=500, error_code="STORAGE_ERROR")
