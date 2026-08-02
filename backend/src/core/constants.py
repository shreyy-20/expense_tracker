"""Application constants and default values."""

# API
API_V1_PREFIX = "/api/v1"

# Pagination
DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 20
MAX_PER_PAGE = 100

# Validation
MIN_TITLE_LENGTH = 1
MAX_TITLE_LENGTH = 100
MIN_AMOUNT = 0.01
MAX_AMOUNT = 999_999_999.99

# Sort
ALLOWED_SORT_FIELDS = ["date", "amount", "title", "category", "created_at"]
DEFAULT_SORT_FIELD = "date"
DEFAULT_SORT_ORDER = "desc"

# Default categories
DEFAULT_CATEGORIES = [
    "Food & Dining",
    "Transportation",
    "Housing",
    "Utilities",
    "Healthcare",
    "Entertainment",
    "Shopping",
    "Education",
    "Travel",
    "Personal Care",
    "Insurance",
    "Savings & Investments",
    "Gifts & Donations",
    "Other",
]

# Default settings
DEFAULT_CURRENCY = "USD"

# Storage
STORAGE_VERSION = 1

# Category limits
MAX_CATEGORIES = 50
MIN_CATEGORY_LENGTH = 1
MAX_CATEGORY_LENGTH = 50
