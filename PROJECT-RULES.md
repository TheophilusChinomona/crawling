# PROJECT-RULES.template

(Template for project-specific rules. Copy this into each repo as `PROJECT-RULES.md`.)

- **Project name:** Crawling
- **Repo URL:** https://github.com/TheophilusChinomona/crawling.git
- **Owner:** Theo (with Byte as coding assistant)
- **Stack:** Multi-language platform: C#/.NET 8 backend API + Python Crawlee crawler + React/TypeScript frontend + SQL Server

## Branch & Git rules
- `main`/`master` is protected.
- Byte never commits directly to `main`/`master`.
- Byte always works on `feature/*`, `fix/*`, `chore/*` branches.
- Each branch results in a PR for Theo to review.

## Environments & safety
- Byte uses local + staging/test by default.
- Prod edits/migrations/deploys only if explicitly allowed here by Theo.
- No logging of secrets or full sensitive payloads.

## Testing expectations
- For non-trivial changes, add/update tests and ensure they pass.

## Collaboration structure
- Repo root must have:
  - `TASKS.md`
  - `hand-offs/from-theo.md`
  - `hand-offs/from-byte.md`
  - `PROJECT-RULES.md`

## Sensitive areas
- Deployment/infra and database migration paths are sensitive; Byte should not touch them unless explicitly requested by Theo.
