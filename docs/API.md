# API Reference

**Base URL**: `http://localhost:8000/api/v1`

## General Information
- **Authentication**: None (by design for this project scope)
- **Rate Limiting**: 100 requests/minute per IP address
- **Content-Type**: `application/json`

---

## Error Response Format

All API errors return a standard JSON format:
```json
{
  "detail": "Error message description",
  "code": "ERROR_CODE",
  "path": "/api/v1/resource"
}
```

---

## Pagination Envelope

List endpoints return a paginated envelope:
```json
{
  "items": [...],
  "total": 150,
  "page": 1,
  "size": 50,
  "pages": 3
}
```

---

## Endpoints

### `GET /api/v1/expenses`
Retrieve a paginated list of expenses.

**Query Parameters:**
- `page` (int, default: 1): Page number
- `per_page` (int, default: 50): Items per page
- `category` (string, optional): Filter by category
- `search` (string, optional): Search in title or notes
- `sort_by` (string, default: "date"): Sort field (date, amount, title)
- `sort_order` (string, default: "desc"): "asc" or "desc"
- `date_from` (string, optional): ISO date string
- `date_to` (string, optional): ISO date string
- `amount_min` (float, optional): Minimum amount
- `amount_max` (float, optional): Maximum amount

**Response (200 OK):**
```json
{
  "items": [
    {
      "id": "abc-123",
      "title": "Coffee",
      "amount": 4.50,
      "currency": "USD",
      "category": "Food",
      "date": "2023-10-01T08:30:00Z",
      "notes": "Morning coffee"
    }
  ],
  "total": 1,
  "page": 1,
  "size": 50,
  "pages": 1
}
```

---

### `POST /api/v1/expenses`
Create a new expense.

**Request Body:**
```json
{
  "title": "Internet Bill",
  "amount": 59.99,
  "currency": "USD",
  "category": "Utilities",
  "date": "2023-10-05T12:00:00Z",
  "notes": "Monthly gigabit internet"
}
```

**Response (201 Created):**
Returns the created expense object with `id`.

---

### `GET /api/v1/expenses/{id}`
Get a specific expense by ID.

**Response (200 OK):** Expense object.
**Response (404 Not Found):** If ID does not exist.

---

### `PUT /api/v1/expenses/{id}`
Replace an entire expense record.

**Request Body:** Full expense object (excluding ID).
**Response (200 OK):** Updated expense object.

---

### `PATCH /api/v1/expenses/{id}`
Partially update an expense record.

**Request Body:** Partial expense object.
**Response (200 OK):** Updated expense object.

---

### `DELETE /api/v1/expenses/{id}`
Delete an expense by ID.

**Response (204 No Content)**

---

### `DELETE /api/v1/expenses`
Bulk delete expenses.

**Request Body:**
```json
{
  "ids": ["id-1", "id-2"]
}
```
**Response (200 OK):**
```json
{
  "deleted_count": 2
}
```

---

### `POST /api/v1/expenses/export`
Export all data as JSON.

**Response (200 OK):** Downloads `expenses.json`.

---

### `POST /api/v1/expenses/import`
Import data from JSON.

**Request Body:** `multipart/form-data` with `file`.
**Response (200 OK):** `{"message": "Import successful", "count": 45}`

---

### `GET /api/v1/categories`
List all custom categories.

**Response (200 OK):** Array of category strings.

---

### `POST /api/v1/categories`
Create a new custom category.

**Request Body:** `{"name": "Entertainment"}`
**Response (201 Created)**

---

### `DELETE /api/v1/categories/{name}`
Delete a custom category.

**Response (204 No Content)**

---

### `GET /api/v1/stats/summary`
Get overall totals and averages.

**Response (200 OK):**
```json
{
  "total_expenses": 1450.50,
  "average_expense": 45.32,
  "count": 32
}
```

---

### `GET /api/v1/stats/monthly`
Get aggregated expenses by month.

**Response (200 OK):** Array of `{ "month": "2023-10", "total": 1450.50 }`.

---

### `GET /api/v1/stats/categories`
Get expense breakdown by category.

**Response (200 OK):** Array of `{ "category": "Food", "total": 350.00, "percentage": 24.1 }`.

---

### `GET /api/v1/health`
Health check endpoint for Docker/Orchestrators.

**Response (200 OK):** `{"status": "ok"}`

---

### `GET /api/v1/version`
Get API version info.

**Response (200 OK):** `{"version": "1.0.0"}`
