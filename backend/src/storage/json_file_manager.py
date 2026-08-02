"""Thread-safe, atomic JSON file manager with file locking."""
import json
import os
import tempfile
from datetime import UTC, datetime
from pathlib import Path

from filelock import FileLock

from src.core.constants import DEFAULT_CATEGORIES, DEFAULT_CURRENCY, STORAGE_VERSION
from src.utils.logger import logger


class JsonFileManager:
    def __init__(self, file_path: Path):
        self.file_path = Path(file_path)
        self._lock = FileLock(str(self.file_path) + ".lock", timeout=10)

    def _get_default_data(self) -> dict:
        """Return the default data structure for a new file."""
        return {
            "version": STORAGE_VERSION,
            "last_modified": datetime.now(UTC).isoformat(),
            "settings": {
                "currency": DEFAULT_CURRENCY,
            },
            "categories": list(DEFAULT_CATEGORIES),
            "expenses": [],
        }

    def ensure_file_exists(self) -> None:
        """Create the JSON file with default structure if it doesn't exist."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self._write_atomic(self._get_default_data())
            logger.info(f"Created new data file: {self.file_path}")

    def read_data(self) -> dict:
        """Read and return the full JSON data structure. Thread-safe."""
        with self._lock:
            try:
                with open(self.file_path, encoding="utf-8") as f:
                    data = json.load(f)
                return data
            except (json.JSONDecodeError, FileNotFoundError) as e:
                logger.warning(f"Data file corrupted or missing, resetting: {e}")
                default = self._get_default_data()
                self._write_atomic(default)
                return default

    def write_data(self, data: dict) -> None:
        """Atomically write data to JSON file. Thread-safe."""
        with self._lock:
            data["last_modified"] = datetime.now(UTC).isoformat()
            self._write_atomic(data)

    def _write_atomic(self, data: dict) -> None:
        """Write to temp file then rename for atomicity."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd, tmp_path = tempfile.mkstemp(
                dir=str(self.file_path.parent),
                suffix=".tmp"
            )
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False, default=str)
                os.replace(tmp_path, str(self.file_path))
            except Exception:
                # Clean up temp file on failure
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
                raise
        except Exception as e:
            logger.error(f"Failed to write data file: {e}")
            raise

    def is_healthy(self) -> bool:
        """Check if storage is readable and writable."""
        try:
            data = self.read_data()
            return isinstance(data, dict) and "expenses" in data
        except Exception:
            return False
