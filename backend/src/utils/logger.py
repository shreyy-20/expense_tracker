import logging
import sys
from src.core.config import get_settings

def setup_logger(name: str = "expense_tracker") -> logging.Logger:
    """Configure and return a structured logger."""
    try:
        settings = get_settings()
        log_level = getattr(logging, settings.log_level.upper())
    except Exception:
        log_level = logging.INFO

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

# Module-level logger for convenience
logger = setup_logger()
