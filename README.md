# 💰 Smart Expense Tracker

> A production-ready, full-stack expense tracking application with beautiful analytics

![CI Status](https://img.shields.io/github/actions/workflow/status/username/smart-expense-tracker/ci.yml?branch=main)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![React](https://img.shields.io/badge/react-18-blue.svg)
![TypeScript](https://img.shields.io/badge/typescript-blue.svg)
![Docker](https://img.shields.io/badge/docker-blue.svg)

## 📸 Screenshots
<!-- Screenshots will be added after UI implementation -->
*(See `assets/screenshots/` for UI designs)*

## ✨ Features

- **✨ Beautiful, responsive dashboard** with real-time statistics
- **📊 Interactive charts** (monthly trends, category breakdown)
- **🌍 Multi-currency support** (any ISO 4217 currency)
- **🌙 Dark/Light mode** with system preference detection
- **🔍 Full-text search**, filtering, sorting, and pagination
- **📁 Custom categories** with color coding
- **📤 Export/Import** expenses as JSON
- **🐳 Fully containerized** with Docker
- **✅ Comprehensive test coverage** (80%+)
- **📖 Auto-generated API documentation** (Swagger + ReDoc)
- **🚀 CI/CD** with GitHub Actions
- **🔒 Security**: Input validation, rate limiting, CORS, security headers

## 🛠️ Tech Stack

| Layer | Technologies |
| --- | --- |
| **Frontend** | React 18, TypeScript, Vite, Tailwind CSS, TanStack Query, Recharts, Lucide React |
| **Backend** | Python 3.11, FastAPI, Pydantic v2, Uvicorn |
| **Testing** | pytest, Vitest, React Testing Library |
| **DevOps** | Docker, GitHub Actions, Vercel, Render |

## 🚀 Quick Start

### Prerequisites
- Node.js 20+
- Python 3.11+
- Docker (optional but recommended)

### Option 1: Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/username/smart-expense-tracker.git
cd smart-expense-tracker

# Start the application
docker-compose up -d
```
Visit `http://localhost:3000` to access the application.

### Option 2: Manual Setup

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
make seed  # Seed the database with sample data
uvicorn src.main:app --reload
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 📁 Project Structure

```
smart-expense-tracker/
├── backend/          # FastAPI application
│   ├── src/          # Application code (routers, models, services)
│   ├── tests/        # Pytest test suite
│   ├── data/         # JSON persistence layer
│   └── requirements.txt
├── frontend/         # React SPA
│   ├── src/          # Components, hooks, context, api
│   ├── public/       # Static assets
│   └── package.json
├── docs/             # Detailed documentation
├── .github/          # CI/CD workflows
├── docker-compose.yml
└── README.md
```

## 📚 API Documentation

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/v1/expenses` | List all expenses with filtering and pagination |
| POST | `/api/v1/expenses` | Create a new expense |
| GET | `/api/v1/expenses/{id}` | Get a specific expense |
| PUT | `/api/v1/expenses/{id}` | Update an expense |
| DELETE | `/api/v1/expenses/{id}` | Delete an expense |
| GET | `/api/v1/stats/summary` | Get expense summary statistics |

- **Swagger UI**: Available at `http://localhost:8000/docs`
- **ReDoc**: Available at `http://localhost:8000/redoc`
- **Full Reference**: See [docs/API.md](docs/API.md)

## 🏗️ Architecture

The application follows a clean 3-layer architecture (Routers, Services, Repositories) ensuring separation of concerns and testability. The data is persisted using a thread-safe JSON file approach, meeting the lightweight requirement without needing a database server.

For a deep dive into the architecture decisions, read [docs/Architecture.md](docs/Architecture.md).

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest --cov=src tests/
```

### Frontend Tests
```bash
cd frontend
npm run test
npm run test:coverage
```

We maintain a strict requirement of 80%+ test coverage across the stack.

## 🚢 Deployment

The application is designed to be easily deployed to modern PaaS providers:
- **Frontend**: Vercel (via GitHub integration)
- **Backend**: Render (using Docker environments)

For full deployment instructions, see [docs/Deployment.md](docs/Deployment.md).

## 🤝 Contributing

We welcome contributions! Please see [docs/Contributing.md](docs/Contributing.md) for guidelines on how to submit pull requests, report issues, and our development standards.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the blazing fast backend framework.
- [React](https://reactjs.org/) and [Tailwind CSS](https://tailwindcss.com/) for the fantastic UI tools.
- [Lucide Icons](https://lucide.dev/) for beautiful SVG icons.
