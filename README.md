# 💰 Smart Expense Tracker

> A production-ready full-stack expense tracker with analytics, Docker support, and CI/CD deployment hooks for Vercel and Render.

![CI Status](https://img.shields.io/github/actions/workflow/status/shreyy-20/expense_tracker/ci.yml?branch=main)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![React](https://img.shields.io/badge/react-18-blue.svg)
![TypeScript](https://img.shields.io/badge/typescript-blue.svg)
![Docker](https://img.shields.io/badge/docker-blue.svg)

## ✨ What the app does

Smart Expense Tracker helps users manage personal or small-business expenses through a polished dashboard and a REST API.

### Current capabilities
- Dashboard with summary statistics and trend views
- Expense management with create, update, delete, bulk delete, and search/filter/sort support
- Category management and user-configurable settings
- Import/export of expense data in JSON format
- Multi-currency-friendly UI and theme support
- Request ID, CORS, and security headers middleware for safer API behavior
- Docker-based local development and deployment paths
- GitHub Actions workflows for CI and deployment hooks

## 🛠️ Tech stack

| Layer | Technologies |
| --- | --- |
| Frontend | React 18, TypeScript, Vite, Tailwind CSS, TanStack Query, React Router, Recharts |
| Backend | Python 3.11, FastAPI, Pydantic v2, Uvicorn, SlowAPI |
| Testing | pytest, Vitest, React Testing Library |
| DevOps | Docker, Docker Compose, GitHub Actions, Vercel, Render |

## 🚀 Quick start

### Prerequisites
- Node.js 20+
- Python 3.11+
- Docker (optional but recommended)

### Option 1: Docker (recommended)
```bash
git clone https://github.com/shreyy-20/expense_tracker.git
cd expense_tracker
cp .env.example .env
docker compose up --build
```

Open:
- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs

### Option 2: Manual setup

#### Backend
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m scripts.seed
uvicorn src.main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📁 Project structure

```text
expense_tracker/
├── backend/
│   ├── src/                # FastAPI app, routers, services, repositories, schemas
│   ├── tests/              # pytest suite
│   ├── data/               # JSON persistence files
│   └── requirements*.txt
├── frontend/
│   ├── src/                # React app, pages, hooks, context, API client
│   └── package.json
├── docs/                   # Architecture, API, deployment, and contributor docs
├── .github/workflows/      # CI and deployment workflows
├── docker-compose.yml      # Full-stack container setup
└── README.md
```

## 📚 API overview

The backend exposes a versioned API under `/api/v1`.

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/v1/health` | Health check |
| GET | `/api/v1/expenses` | List expenses with filtering, sorting, and pagination |
| POST | `/api/v1/expenses` | Create an expense |
| GET | `/api/v1/expenses/{id}` | Fetch one expense |
| PUT | `/api/v1/expenses/{id}` | Replace an expense |
| PATCH | `/api/v1/expenses/{id}` | Partially update an expense |
| DELETE | `/api/v1/expenses/{id}` | Delete an expense |
| DELETE | `/api/v1/expenses` | Bulk delete expenses |
| POST | `/api/v1/expenses/export` | Export expenses |
| POST | `/api/v1/expenses/import` | Import expenses |
| GET | `/api/v1/stats/summary` | Get summary statistics |

Swagger and ReDoc are available at:
- http://localhost:8000/docs
- http://localhost:8000/redoc

## 🧪 Testing and quality checks

### Backend
```bash
cd backend
pytest
ruff check src tests
ruff format --check src tests
```

### Frontend
```bash
cd frontend
npm run build
npm run test
npx eslint src --ext .ts,.tsx
```

## 🚢 Deployment

The repository includes deployment-ready configuration for both hosting providers:
- Frontend: Vercel via the Vite build output in `frontend/dist`
- Backend: Render using the Docker-based service definition in `render.yaml`

### GitHub Actions
The deployment workflow uses deploy hooks for Vercel and Render and performs smoke checks against the deployed URLs. Configure these repository secrets before enabling deployments:
- `VERCEL_DEPLOY_HOOK_URL`
- `RENDER_DEPLOY_HOOK_URL`
- `BACKEND_URL`
- `FRONTEND_URL`

For full deployment instructions, see [docs/Deployment.md](docs/Deployment.md).

## 🤝 Contributing

Contributions are welcome. Please review [docs/Contributing.md](docs/Contributing.md) for workflow guidance and coding standards.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
