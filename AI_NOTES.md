# AI-Assisted Development Notes

## Overview
This project was developed with AI assistance (GitHub Copilot, ChatGPT/Claude). This document provides full transparency on which parts were AI-assisted and which were manually written or modified.

## Files AI Helped Generate
- Initial project scaffolding (folder structure, config files)
- Pydantic schema definitions (`schemas/*.py`) — AI generated initial schemas, I manually added custom validators for currency and amount precision.
- Docker configurations — AI generated base Dockerfiles, I manually optimized multi-stage builds and added healthchecks.
- CI/CD workflows — AI generated the GitHub Actions YAML, I manually added caching strategies and deployment secrets config.
- Test boilerplate — AI generated test structure, I manually wrote specific edge case tests.
- Tailwind component styling — AI suggested initial class combinations, I refined spacing, colors, and animations manually.
- API endpoint structure — AI generated CRUD boilerplate, I manually added pagination logic, filtering, and error handling.

## What I Manually Built/Changed
- Complete architecture decisions and layer separation.
- JSON file manager with atomic writes and file locking (AI didn't handle concurrency correctly).
- Statistics service aggregation logic (AI-generated version had floating point precision issues).
- Category color system and design token mapping.
- Dark mode implementation with CSS custom properties.
- Responsive sidebar behavior and mobile navigation.
- Export/Import validation and error recovery.
- All edge case handling (negative amounts, empty states, concurrent writes).
- Custom hook composition patterns (`useExpenses` combining query + mutation + cache invalidation).

## Bugs Found in AI-Generated Code
1. AI suggested using `json.dump` without `ensure_ascii=False` — broke Unicode characters in expense titles.
2. Initial Pydantic model used `float` for amount without rounding — caused $4.999999999 display issues. Fixed with custom validator rounding to 2 decimal places.
3. AI-generated CORS middleware used wildcard `*` origin — replaced with explicit origin allowlist.
4. Rate limiter was applied per-route instead of globally — refactored to middleware.
5. React Query cache invalidation was missing after bulk delete — added manual cache invalidation.
6. AI suggested storing dates as strings without timezone info — switched to ISO 8601 with proper parsing.

## What I Rejected and Why
1. **SQLAlchemy ORM**: AI suggested adding SQLAlchemy even though the requirement was JSON persistence. Rejected as unnecessary abstraction over a JSON file.
2. **Redux Toolkit**: AI recommended Redux for state management. Rejected in favor of TanStack Query (server state) + Context (UI state) — Redux would add ~200KB and unnecessary boilerplate for this scope.
3. **Helmet.js**: AI suggested adding Helmet for security headers. Rejected because we're using nginx in production which handles headers, and FastAPI middleware handles it in dev.
4. **Moment.js**: AI suggested Moment.js for date formatting. Rejected in favor of native `Intl.DateTimeFormat` — zero bundle size, better i18n support.
5. **Custom authentication system**: AI generated a full JWT auth system. Rejected as out of scope — assignment doesn't require auth, and adding it would over-engineer the solution.

## AI Usage Philosophy
I used AI as a coding accelerator, not a replacement for engineering judgment. Every AI suggestion was reviewed, tested, and often modified before inclusion. Architecture decisions, design patterns, and security considerations were driven by my own engineering experience.
