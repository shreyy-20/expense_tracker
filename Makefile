.PHONY: help dev dev-backend dev-frontend install install-backend install-frontend test test-backend test-frontend lint lint-backend lint-frontend format format-backend build up down logs clean seed docker-build docker-up docker-down

# Show help output
help:
	@echo "Available targets:"
	@echo "  help             - Show this help message"
	@echo "  dev              - Start both backend and frontend in dev mode"
	@echo "  dev-backend      - Start backend in dev mode"
	@echo "  dev-frontend     - Start frontend in dev mode"
	@echo "  install          - Install all dependencies"
	@echo "  install-backend  - Install backend dependencies"
	@echo "  install-frontend - Install frontend dependencies"
	@echo "  test             - Run all tests"
	@echo "  test-backend     - Run backend tests"
	@echo "  test-frontend    - Run frontend tests"
	@echo "  lint             - Run all linters"
	@echo "  lint-backend     - Run backend linter"
	@echo "  lint-frontend    - Run frontend linter"
	@echo "  format           - Format all code"
	@echo "  format-backend   - Format backend code"
	@echo "  build            - Build production Docker images"
	@echo "  up               - docker-compose up -d"
	@echo "  down             - docker-compose down"
	@echo "  logs             - docker-compose logs -f"
	@echo "  clean            - Remove build artifacts and caches"
	@echo "  seed             - Run backend seed script"
	@echo "  docker-build     - Build docker images using compose"
	@echo "  docker-up        - Start docker compose services"
	@echo "  docker-down      - Stop and remove docker compose services/volumes"

# Start dev environments (requires background jobs setup like concurrently or separate terminals usually, using simple approach here)
dev: dev-backend dev-frontend

dev-backend:
	cd backend && uvicorn src.main:app --reload --port 8000

dev-frontend:
	cd frontend && npm run dev

# Installation
install: install-backend install-frontend

install-backend:
	cd backend && pip install -r requirements.txt -r requirements-dev.txt

install-frontend:
	cd frontend && npm install

# Testing
test: test-backend test-frontend

test-backend:
	cd backend && pytest -v --cov=src --cov-report=term-missing

test-frontend:
	cd frontend && npx vitest run --coverage

# Linting
lint: lint-backend lint-frontend

lint-backend:
	cd backend && ruff check src/ tests/

lint-frontend:
	cd frontend && npx eslint src/ --ext .ts,.tsx

# Formatting
format: format-backend

format-backend:
	cd backend && ruff format src/ tests/

# Docker tasks
build:
	docker build -t smart-expense-backend ./backend
	docker build -t smart-expense-frontend ./frontend

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

clean:
	rm -rf backend/build backend/dist backend/*.egg-info backend/.pytest_cache backend/htmlcov backend/.coverage backend/__pycache__ backend/*/__pycache__
	rm -rf frontend/dist frontend/.vite frontend/node_modules
	rm -rf node_modules

seed:
	cd backend && python -m scripts.seed

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down -v
