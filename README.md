# LeadCrawl -- Developer Guide

This guide walks you through the development workflow for the LeadCrawl project using **agent-os** and **Claude Code**. Follow it step by step.

> Collaboration note: Byte/Theo project collaboration files live at `PROJECT-RULES.md`, `TASKS.md`, and `hand-offs/`.

---

## Project Overview

LeadCrawl is a web crawling platform that helps sales teams generate qualified leads. It crawls public websites, extracts professional contact data, validates and deduplicates it, and presents clean leads through a web dashboard.

**Tech Stack:**
- Backend: C# / .NET 8, ASP.NET Core Web API, Entity Framework Core 8, Hangfire
- Crawler: Python 3.10+, Crawlee (BeautifulSoup + Playwright) — see [crawler/README.md](crawler/README.md)
- Frontend: React 18+ (Vite), TypeScript, shadcn/ui, Tailwind CSS
- Database: SQL Server
- Auth: ASP.NET Core Identity + JWT

---

## Project Structure

```
Crawling/
├── README.md                  # This file -- start here
├── crawler/                   # Crawlee (Python) crawling engine — see crawler/README.md
│   ├── pyproject.toml
│   ├── README.md              # Install, run, and .NET integration
│   └── src/leadcrawl_crawler/ # Package: runner, handlers
├── pdf2markdown/              # Standalone PDF to markdown (vision-parse) — see pdf2markdown/README.md
├── agent-os/                  # The brain of the workflow system
│   ├── product/               # Product planning docs
│   │   ├── mission.md         # What we're building and why
│   │   ├── roadmap.md         # Feature list in priority order
│   │   └── tech-stack.md      # All technology choices explained
│   ├── specs/                 # Feature specifications (created per feature)
│   │   └── YYYY-MM-DD-name/   # Each spec gets a dated folder
│   │       ├── planning/      # Requirements, visuals, research
│   │       ├── spec.md        # The detailed spec document
│   │       └── tasks.md       # Broken-down implementation tasks
│   ├── commands/              # Workflow definitions (don't edit these)
│   └── standards/             # Coding standards for backend, frontend, testing
├── tasks/                     # PRDs and task tracking
│   └── prd-leadcrawl.md       # Product Requirements Document
└── .claude/                   # Claude Code project config
```

---

## Research agent tools

**crawler/** and **pdf2markdown/** are **standalone, independent** tools. They have no code dependency on each other and can be used alone or together in pipelines (e.g. crawl docs + convert PDFs to markdown).

For research agents and automation:

- **Web crawling:** Project skill [.cursor/skills/web-crawler/SKILL.md](.cursor/skills/web-crawler/SKILL.md) describes when and how to run the crawler. Tool: `crawler/` — see [crawler/README.md](crawler/README.md).
- **PDF to markdown:** Project skill [.cursor/skills/pdf2markdown/SKILL.md](.cursor/skills/pdf2markdown/SKILL.md) describes when and how to run PDF conversion. Tool: `pdf2markdown/` — see [pdf2markdown/README.md](pdf2markdown/README.md).

Both skills can be copied or referenced as reusable skills elsewhere. See [RESEARCH-TOOLS.md](RESEARCH-TOOLS.md) for a short reference of entrypoints and usage.

---

## How the Workflow Works

The agent-os system follows a **linear pipeline**. Each step feeds into the next. Don't skip steps.

```
1. Plan Product    -->  mission, roadmap, tech stack
2. Write PRD       -->  detailed requirements with user stories
3. Shape Spec      -->  research and requirements for ONE feature
4. Write Spec      -->  detailed spec document for that feature
5. Create Tasks    -->  break the spec into implementable task groups
6. Implement Tasks -->  build it, test it, verify it
```

Steps 1 and 2 are already done. You start at **Step 3**.

---

## Step-by-Step Workflow

### Step 1: Understand the Product (Already Done)

Read these files to understand what we're building:

| File | What it tells you |
|---|---|
| `agent-os/product/mission.md` | The product vision, target users, problems we solve, key features |
| `agent-os/product/roadmap.md` | All 12 features in priority order. Items 1-9 are the MVP |
| `agent-os/product/tech-stack.md` | Every technology choice and why we picked it |

**Action:** Read all three files before doing anything else.

---

### Step 2: Understand the PRD (Already Done)

Read `tasks/prd-leadcrawl.md`. This is the Product Requirements Document. It contains:

- **12 user stories** with acceptance criteria (checkboxes you'll tick off)
- **22 functional requirements** numbered FR-1 through FR-22
- **Non-goals** so you know what NOT to build
- **Technical considerations** for implementation decisions
- **Open questions** that may need answers before you start

**Action:** Read the PRD thoroughly. If any open question affects the feature you're about to work on, raise it before starting.

---

### Step 3: Pick a Feature from the Roadmap

Open `agent-os/product/roadmap.md`. Features are ordered by dependency -- **work top to bottom**. The first unchecked item is your next feature.

The roadmap for this project:

1. Database Schema & Lead Model
2. Core Crawling Engine
3. Data Extraction Pipeline
4. Smart Filtering & Validation
5. Deduplication Engine
6. Compliance & Audit Logging
7. Backend API
8. Lead Dashboard (Frontend)
9. Crawl Management UI
10. Lead Scoring
11. CRM Export Integration
12. User Authentication & Team Management

**Action:** Identify which feature you're working on. Everything below uses that feature as the input.

---

### Step 4: Shape the Spec

This step gathers detailed requirements for your chosen feature.

**Run in Claude Code:**
```
/agent-os:shape-spec
```

**What happens:**
1. A dated spec folder is created: `agent-os/specs/YYYY-MM-DD-feature-name/`
2. Claude asks you 4-8 clarifying questions about the feature
3. You answer them (reference the PRD user stories for detail)
4. Your answers are saved to `planning/requirements.md`

**What you provide:**
- The feature name and description from the roadmap
- Answers to clarifying questions
- Any mockups or screenshots (drop them into `planning/visuals/`)

**Output:** `agent-os/specs/YYYY-MM-DD-feature-name/planning/requirements.md`

---

### Step 5: Write the Spec

This turns your requirements into a detailed, implementable specification.

**Run in Claude Code:**
```
/agent-os:write-spec
```

**What happens:**
1. Claude reads your requirements and any visuals
2. Searches the codebase for existing patterns to reuse
3. Generates a detailed spec with:
   - Goal statement
   - User stories (up to 3)
   - Specific requirements (up to 10)
   - Existing code to leverage
   - Out of scope items

**Output:** `agent-os/specs/YYYY-MM-DD-feature-name/spec.md`

**Action:** Read the spec. If something is wrong or missing, tell Claude to fix it before moving on.

---

### Step 6: Create Tasks

This breaks the spec into small, implementable task groups.

**Run in Claude Code:**
```
/agent-os:create-tasks
```

**What happens:**
1. Claude reads the spec
2. Creates task groups organized by area (database, API, frontend, testing)
3. Each task group has:
   - Clear description of what to build
   - Sub-tasks with checkboxes
   - 2-8 focused tests per group
   - Dependencies on other task groups

**Output:** `agent-os/specs/YYYY-MM-DD-feature-name/tasks.md`

**Action:** Review the tasks. Make sure they make sense and nothing is missing.

---

### Step 7: Implement Tasks

This is where you build the feature.

**Run in Claude Code:**
```
/agent-os:implement-tasks
```

**What happens:**
1. Claude shows you the task groups and asks which to implement
2. You pick a task group (start with the first one -- they're ordered by dependency)
3. Claude implements it following the codebase standards in `agent-os/standards/`
4. Checkboxes in `tasks.md` are ticked off as work completes
5. Tests are run to verify the implementation
6. A verification report is generated

**Repeat** this step for each task group until the feature is complete.

---

### Step 8: Repeat for the Next Feature

Once a feature is done:
1. Check it off in `agent-os/product/roadmap.md`
2. Go back to **Step 3** and pick the next feature
3. Repeat until the MVP (items 1-9) is complete

---

## Using the PRD During Development

The PRD (`tasks/prd-leadcrawl.md`) is your reference throughout development. Here's how to use it:

| When you're... | Look at... |
|---|---|
| Shaping a spec | The matching **user story** for acceptance criteria |
| Writing validation logic | **FR-5 through FR-8** for exact validation rules |
| Building the lead table | **US-003** for columns, sorting, filtering requirements |
| Adding compliance features | **US-009** and **FR-11 through FR-13** |
| Wondering "should I build this?" | **Non-Goals** section -- if it's listed there, don't build it |
| Making a design decision | **Technical Considerations** for stack-specific guidance |

User Story IDs (US-001 through US-012) and Functional Requirement IDs (FR-1 through FR-22) can be referenced in commits and task descriptions to maintain traceability.

---

## Coding Standards

Before writing code, read the relevant standards in `agent-os/standards/`:

| Area | File | Covers |
|---|---|---|
| All code | `global/coding-style.md` | Naming, formatting, structure |
| All code | `global/conventions.md` | Project conventions |
| All code | `global/error-handling.md` | Error handling patterns |
| All code | `global/validation.md` | Input validation rules |
| Backend | `backend/api.md` | REST API design, endpoints |
| Backend | `backend/models.md` | Entity Framework models |
| Backend | `backend/migrations.md` | Database migrations |
| Backend | `backend/queries.md` | LINQ and query patterns |
| Frontend | `frontend/components.md` | React component patterns |
| Frontend | `frontend/css.md` | Tailwind and styling |
| Frontend | `frontend/accessibility.md` | WCAG compliance |
| Frontend | `frontend/responsive.md` | Responsive breakpoints |
| Testing | `testing/test-writing.md` | Test structure and scope |

---

## Quick Reference: All Commands

| Command | What it does | When to use it |
|---|---|---|
| `/agent-os:plan-product` | Creates mission, roadmap, tech stack | Starting a new project (already done) |
| `/agent-os:shape-spec` | Gathers requirements for a feature | Before writing a spec |
| `/agent-os:write-spec` | Writes a detailed spec from requirements | After shaping |
| `/agent-os:create-tasks` | Breaks a spec into task groups | After writing a spec |
| `/agent-os:implement-tasks` | Implements task groups | After creating tasks |
| `/agent-os:orchestrate-tasks` | Multi-agent task delegation | Advanced: parallel implementation |

---

## Rules

1. **Always work top-to-bottom on the roadmap.** Features are ordered by dependency.
2. **Don't skip the spec step.** Even if a feature seems simple, shape it and write the spec. This catches edge cases early.
3. **Reference the PRD.** User stories and functional requirements are your source of truth for what "done" means.
4. **Read before you write.** Always read existing code and standards before implementing. Don't guess.
5. **One feature at a time.** Finish and verify a feature before starting the next one.
6. **Check the non-goals.** If you're about to build something listed under non-goals in the PRD, stop.
7. **Flag open questions.** If you hit an open question from the PRD during implementation, raise it -- don't assume.
