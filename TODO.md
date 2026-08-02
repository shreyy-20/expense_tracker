# TODO - Fix Progress

## Phase 1: Critical Blockers
- [x] 1. Create root `Dockerfile`
- [x] 2. Fix backend tests (expense_id → id, exception names)
- [x] 3. Fix nginx.conf (configurable proxy_pass)
- [x] 4. Create `.github/workflows/ci.yml`
- [x] 5. Create `.github/workflows/deploy.yml`
- [x] 6. Create `.env.example`

## Phase 2: Configuration Fixes
- [x] 7. Fix docker-compose.dev.yml backend port mapping
- [x] 8. Clean up duplicate vite config files

## Phase 3: Validation
- [x] 9. Run backend tests
- [x] 10. Run backend lint (ruff)
- [x] 11. Run frontend lint (eslint, tsc)
- [x] 12. Build Docker images
- [x] 13. Run & verify containers
- [x] 14. Verify health endpoints
