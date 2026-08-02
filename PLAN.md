# Comprehensive Audit & Fix Plan

## Issues Found During Audit

### CRITICAL ISSUES

#### 1. Root Dockerfile is EMPTY (0 bytes) — BLOCKING RENDER DEPLOY
- `render.yaml` references `./Dockerfile` (root Dockerfile) for backend service
- File is empty → Render deployment will fail immediately
- **Fix:** Create proper root Dockerfile that builds the backend

#### 2. Backend Tests Fail — Wrong Exception Names & Model Parameters
- `test_expense_repository.py` passes `expense_id=...` to `Expense()` constructor, but model expects `id=...`
- `test_expense_service.py` imports `NotFoundError` and `ValidationError` — actual names are `NotFoundException` and `ValidationException`
- **Fix:** Correct test code to match actual API

#### 3. nginx.conf Hardcodes `backend:8000` Upstream — BLOCKING STANDALONE DEPLOY
- Frontend nginx proxy_pass `http://backend:8000` requires Docker DNS resolution
- Running standalone (Vercel/Render) will crash nginx
- **Fix:** Make proxy_pass configurable via environment variable

#### 4. No `.github/workflows/` Directory Exists
- CI/CD workflows are missing from the repository
- **Fix:** Create proper GitHub Actions CI and deploy workflows

#### 5. No `.env.example` File
- Required for documentation and setup
- **Fix:** Create comprehensive `.env.example`

### MEDIUM ISSUES

#### 6. Frontend Docker Build Context Too Large (no .dockerignore initially)
- `.dockerignore` files now created but need verification

#### 7. `docker-compose.dev.yml` Missing Port Mapping for Backend
- Backend service has no `ports:` exposing it to host

#### 8. Backend `conftest.py` May Have Settings Caching Issues
- `get_settings.cache_clear()` order may not work correctly

#### 9. Vite Config Has Both `vite.config.ts` and `vite.config.js` and `vite.config.d.ts`
- Potential confusion or duplicate configs

### MINOR ISSUES

#### 10. Frontend `tsconfig.node.json` references not verified
#### 11. `package-lock.json` may have vulnerabilities
#### 12. Backend `pyproject.toml` missing `[project.dependencies]` section

---

## Fix Plan

### Phase 1: Critical Fixes
1. Create root `Dockerfile` for backend (multi-stage build)
2. Fix backend tests: `expense_id` → `id`, `NotFoundError` → `NotFoundException`
3. Fix nginx.conf to use env variable for API proxy
4. Create `.github/workflows/ci.yml` and `.github/workflows/deploy.yml`
5. Create `.env.example`

### Phase 2: Configuration Fixes
6. Fix docker-compose.dev.yml port mapping
7. Clean up duplicate vite config files
8. Verify frontend build works end-to-end

### Phase 3: Validation
9. Run backend tests
10. Run frontend tests
11. Run backend lint (ruff)
12. Run frontend lint (eslint, tsc)
13. Build Docker images
14. Run Docker containers
15. Verify health checks

### Phase 4: Deployment
16. Commit changes
17. Verify GitHub Actions CI
18. Verify Vercel deployment
19. Verify Render deployment
