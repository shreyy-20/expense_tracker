from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App
    app_name: str = "Smart Expense Tracker"
    app_version: str = "1.0.0"
    environment: str = "development"  # development | production | testing
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "info"
    
    # CORS
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    
    # Data
    data_dir: str = "./data"
    
    # Rate limiting
    rate_limit: str = "100/minute"
    
    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    @property
    def data_file_path(self) -> Path:
        return Path(self.data_dir) / "expenses.json"
    
    model_config = SettingsConfigDict(
        env_prefix="BACKEND_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
