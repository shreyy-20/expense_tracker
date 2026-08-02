# Contributing Guidelines

Thank you for your interest in contributing to the Smart Expense Tracker! We welcome bug reports, feature requests, and pull requests.

## Getting Started

1.  **Fork** the repository on GitHub.
2.  **Clone** your fork locally: `git clone https://github.com/your-username/smart-expense-tracker.git`
3.  **Create a branch** for your feature or bug fix: `git checkout -b feature/awesome-new-feature` or `git checkout -b fix/annoying-bug`.

## Development Setup

See the [README](../README.md#quick-start) for instructions on how to run the application locally using Docker or manual installation.

## Code Style

### Backend (Python)
-   We use **Ruff** for linting and formatting.
-   Run `ruff check .` to check for issues and `ruff format .` to format code.
-   Follow PEP 8 guidelines.
-   Ensure type hints are used everywhere.

### Frontend (TypeScript/React)
-   We use **ESLint** and **Prettier**.
-   Run `npm run lint` and `npm run format`.
-   Use functional components and hooks. No class components.
-   Ensure strict typing with TypeScript. Avoid `any`.

## Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
-   `feat: add dark mode support`
-   `fix: resolve crash on invalid date format`
-   `docs: update API documentation`
-   `test: add unit tests for stats service`
-   `refactor: optimize JSON file parsing`

## Pull Request Process

1.  Ensure your code follows the coding style.
2.  Ensure all existing tests pass.
3.  Write new tests for your features or bug fixes. Coverage must remain above 80%.
4.  Update documentation (README, API docs) if your changes require it.
5.  Submit a Pull Request targeting the `main` branch.
6.  A maintainer will review your code, request changes if necessary, and merge it.

## Testing Requirements

-   **Backend**: Run tests via `pytest`. All API endpoints must have corresponding integration tests.
-   **Frontend**: Run tests via `vitest`. Complex logic (like hooks and utilities) must be unit-tested. Core UI flows should have basic component tests.

## Adding New Features Checklist

Before adding a new feature, ask yourself:
- [ ] Does this fit the scope of a lightweight expense tracker?
- [ ] Have I created tests for the new logic?
- [ ] Are the UI components responsive?
- [ ] Did I update the relevant API documentation?

## Reporting Bugs

Please open an issue on GitHub using the "Bug Report" template. Include:
-   Expected behavior vs Actual behavior
-   Steps to reproduce
-   Browser/OS details
-   Screenshots if applicable

## Code of Conduct

Please be respectful and professional in all interactions. Harassment or abusive behavior will not be tolerated.
