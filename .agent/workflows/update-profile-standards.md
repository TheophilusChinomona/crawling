---
description: Workflow: Update Profile Standards (Windows C:\ scan + per-file approvals)
---

---
description: Update profile standards one file at a time with explicit approval gates (Windows C:\ scanning)
---

# Workflow: Update Profile Standards (Windows C:\ scan + per-file approvals)

## Purpose
Update Agent OS profile standards one file at a time:
- find the base `agent-os` folder on Windows (C:\)
- select which profile to edit
- iterate every `standards/**/*.md` file
- ask questions + draft changes
- only write changes after explicit approval per file

## Guardrails (non-negotiable)
- Do NOT edit the `default` profile directly unless the user explicitly insists.
- One file at a time. No batch approvals.
- Every file requires explicit: APPROVE / EDIT / SKIP before moving on.
- Keep standards actionable: MUST/SHOULD language + examples.
- Don't change folder structure unless user approves.

---

## Step 0 — Locate base Agent OS on Windows (C:\)
Goal: find the folder that contains `profiles/`, `scripts/`, `commands/`, etc.

### 0.1 First try: fast known locations
Check these common paths:
- `C:\Users\theoc\agent-os` (confirmed location)
- `C:\Users\<YOU>\agent-os`
- `C:\Users\<YOU>\Documents\agent-os`
- `C:\agent-os`

### 0.2 If not found: search C:\ for an `agent-os` folder
Run ONE of these:

**PowerShell (recommended):**
- `Get-ChildItem -Path C:\ -Directory -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -eq "agent-os" } | Select-Object -First 10 FullName`

**Windows CMD:**
- `dir C:\agent-os /s /b`
- or: `dir C:\ /s /b | findstr /i "\\agent-os$"`

### 0.3 Confirm it's the base install
Open the found folder and verify it contains:
- `profiles\`
- `scripts\`
If it doesn't, keep searching.

**Output of this step:**
- Set `AGENT_OS_ROOT = <full path>` (example: `C:\Users\Tino\agent-os`)

Approval Gate:
- Ask the user to confirm: "Is this the correct Agent OS root folder? (YES/NO)"

---

## Step 1 — Ask which profile to edit (selection gate)
1) List available profiles in:
   `<AGENT_OS_ROOT>\profiles\`

2) Ask the user:
   "Which profile do you want to edit?"

Rules:
- If the user chooses `default`, warn:
  - best practice is create a custom profile and copy overrides
  - continue only if they confirm they still want `default`

(Agent OS supports profile creation via scripts; new profiles typically override only what's needed.) 

Approval Gate:
- "Proceed editing profile: <PROFILE_NAME>? (YES/NO)"

---

## Step 2 — Inventory standards files (ordered checklist)
1) Standards root:
   `<AGENT_OS_ROOT>\profiles\<PROFILE_NAME>\standards\`

2) Collect all `*.md` under `standards\**\*.md`

3) Stable order:
- `global\` then `backend\` then `frontend\` then `testing\`
- alphabetical within each folder

4) Show the checklist to the user.

Approval Gate:
- "Proceed with this file order? (YES/NO)"

---

## Step 3 — Loop: update one standards file at a time

For each file in the checklist:

### 3.1 Read + summarize
- Summarize in 5–10 bullets:
  - what it governs
  - top MUST rules
  - top SHOULD rules
  - examples present/missing
  - anything unclear or conflicting

### 3.2 Ask targeted questions (minimum needed)
Ask only what's needed to revise confidently. Default questions:
1) Scope: "What code does this apply to (folders, layers, projects)?"
2) Top 3 MUST rules you care about most?
3) Any tooling constraints (linting/formatting/testing)?
4) Any conventions you want enforced (naming, error handling, logging, etc.)?
5) Common mistakes to prevent?

Special case:
- If the file is a "stack" or "global conventions" standard, ask stack-defining questions instead (runtime, framework, styling, data, testing, deployment).

### 3.3 Draft revision
Produce a full replacement draft of the file with:
- Clear title + short purpose
- Rules grouped by theme
- MUST/SHOULD wording
- 1–3 concrete examples (where relevant)
- "Common pitfalls" section (if relevant)

Also provide a short "Diff summary":
- Added:
- Changed:
- Removed:

### 3.4 Per-file Approval Gate
User must choose exactly one:
- APPROVE (write to disk)
- EDIT (tell me changes; I re-draft; repeat gate)
- SKIP (don't modify; move on)

### 3.5 Write + quick validation (only after APPROVE)
- Write updated content to the same file path.
- Validate:
  - headings consistent
  - Markdown clean
  - examples readable

---

## Step 4 — End summary
Produce:
- Changed files (1-line each)
- Skipped files (reason)
- Follow-ups (tooling/config suggestions) — do not apply unless asked

Optional Gate:
- "Create `standards\CHANGELOG.md` with today's changes? (YES/NO)"
