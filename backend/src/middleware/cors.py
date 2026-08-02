"""CORS middleware configuration."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import get_settings


def setup_cors(app: FastAPI) -> None:
    settings = get_settings()
    origins = settings.cors_origins_list

    if "*" in origins or len(origins) == 0:
        allow_origins = ["*"]
        allow_credentials = False
    else:
        allow_origins = origins
        allow_credentials = True

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=allow_credentials,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Request-ID"],
    )
