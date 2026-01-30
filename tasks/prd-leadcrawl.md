# PRD: LeadCrawl -- Sales Lead Generation Web Crawler

## Introduction

LeadCrawl is a web crawling platform that helps sales teams generate qualified leads by automatically discovering, extracting, and validating professional contact data from public web sources. The platform replaces manual lead research (browsing company websites, copying data from LinkedIn, cross-referencing directories) with an automated pipeline that crawls, extracts, validates, deduplicates, and presents clean lead data through a web dashboard.

The crawler is configurable -- users can target company websites, public business directories, LinkedIn profiles, or any public URL. All collected data is filtered for quality and logged for compliance with POPIA, GDPR, CAN-SPAM, and CCPA regulations.

## Goals

- Automate the discovery and extraction of professional contact data from public web sources
- Deliver clean, validated, deduplicated lead records with: Name, Surname, Position, Email, Phone, Company, Department, LinkedIn/Profile URL
- Provide a self-service web dashboard where sales team members can browse, filter, and export leads without technical skills
- Ensure every crawl action is logged and auditable for compliance with POPIA, GDPR, CAN-SPAM, and CCPA
- Reduce time spent on manual lead research by the sales team
- Discard irrelevant, incomplete, or unusable data automatically so the database only contains actionable leads

## User Stories

### US-001: Configure and Launch a Crawl Job
**Description:** As an SDR, I want to create a new crawl job by entering target URLs or domains so the system can discover and extract leads from those sources.

**Acceptance Criteria:**
- [ ] User can enter one or more target URLs or domains
- [ ] User can select source type (company website, directory, LinkedIn, custom URL)
- [ ] User can set crawl depth (how many levels of links to follow)
- [ ] User can set rate-limiting preferences (requests per second)
- [ ] Crawl job is created and queued for execution
- [ ] User sees confirmation with job ID and estimated scope
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

### US-002: Monitor Crawl Progress
**Description:** As an SDR, I want to see the status of my crawl jobs in real time so I know when leads are ready to review.

**Acceptance Criteria:**
- [ ] Dashboard shows list of all crawl jobs with status (queued, running, completed, failed)
- [ ] Running jobs show progress: pages crawled, leads found, errors encountered
- [ ] User can pause or cancel a running crawl job
- [ ] Completed jobs show summary: total pages crawled, leads extracted, leads after validation
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

### US-003: Browse and Search Leads
**Description:** As an SDR, I want to browse all collected leads in a searchable, filterable table so I can find relevant contacts quickly.

**Acceptance Criteria:**
- [ ] Leads displayed in a paginated table with columns: Name, Surname, Position, Company, Email, Phone, Department, Profile URL, Quality Score, Source
- [ ] Table supports sorting by any column
- [ ] Full-text search across all fields
- [ ] Filter by: company, department, position/title, quality score range, date collected, source type
- [ ] Filters persist in URL params
- [ ] Empty state message when no leads match
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

### US-004: View Lead Detail
**Description:** As an SDR, I want to view the full details of a lead including its source and audit trail so I can verify the data before using it.

**Acceptance Criteria:**
- [ ] Lead detail view shows all fields: Name, Surname, Position, Email, Phone, Company, Department, Profile URL(s)
- [ ] Shows quality score with breakdown (completeness, email validity, source reliability)
- [ ] Shows audit info: source URL, crawl timestamp, collection method
- [ ] Shows compliance status and legal basis for collection
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

### US-005: Export Leads as CSV
**Description:** As an SDR, I want to export selected leads or filtered results as a CSV file so I can import them into my outreach tools.

**Acceptance Criteria:**
- [ ] User can select individual leads via checkboxes or select all filtered results
- [ ] "Export CSV" button downloads a CSV file with all lead fields
- [ ] CSV includes headers matching the field names
- [ ] Export is logged in the audit trail (who exported, when, how many records)
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

### US-006: Smart Data Extraction
**Description:** As a system, I need to extract structured contact data from varied page layouts (team pages, about pages, contact pages, directory listings) so the database contains clean, structured records.

**Acceptance Criteria:**
- [ ] Extracts name, surname, position, email, phone, company, department, and profile URLs from crawled pages
- [ ] Handles common page layouts: team grids, staff lists, contact pages, directory entries
- [ ] Uses CSS selectors, regex patterns, and heuristics to identify contact fields
- [ ] Handles variations in field labels (e.g., "Phone", "Tel", "Mobile", "Contact Number")
- [ ] Extracts LinkedIn and other social profile URLs when present
- [ ] Typecheck passes

### US-007: Validate and Filter Extracted Data
**Description:** As a system, I need to validate extracted data and discard unusable records so the lead database only contains actionable contacts.

**Acceptance Criteria:**
- [ ] Email addresses validated for format and domain MX record existence
- [ ] Phone numbers normalized to international format
- [ ] Job titles/positions classified into departments where possible
- [ ] Records missing both email AND phone are discarded
- [ ] Records missing name are discarded
- [ ] Low-confidence extractions flagged for manual review rather than auto-discarded
- [ ] Validation results logged per record
- [ ] Typecheck passes

### US-008: Deduplicate Leads
**Description:** As a system, I need to detect and merge duplicate leads so the database stays clean across multiple crawl jobs.

**Acceptance Criteria:**
- [ ] New leads compared against existing records before insertion
- [ ] Fuzzy matching on name + email + company to detect duplicates
- [ ] Exact email match always treated as duplicate
- [ ] Duplicate records merged (newer data fills gaps in older record)
- [ ] Deduplication stats shown in crawl job summary
- [ ] Typecheck passes

### US-009: Compliance Audit Logging
**Description:** As a Sales Manager, I need every data collection action logged so the company can demonstrate legal compliance if audited.

**Acceptance Criteria:**
- [ ] Every collected record tagged with: source URL, crawl timestamp, collection method, legal basis
- [ ] Audit log viewable in the dashboard (filterable by date, source, user)
- [ ] Export audit log as CSV
- [ ] robots.txt respected -- pages disallowed by robots.txt are never crawled
- [ ] Configurable data retention policy with automatic archival/deletion
- [ ] Opt-out list: flagged domains or individuals are never re-crawled
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

### US-010: Lead Quality Scoring
**Description:** As an SDR, I want leads scored by quality so I can prioritize the best ones for outreach.

**Acceptance Criteria:**
- [ ] Each lead assigned a quality score (0-100)
- [ ] Score based on: data completeness, email verification status, source reliability, data recency
- [ ] Score visible in lead table and detail view
- [ ] Leads sortable and filterable by score
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

### US-011: Schedule Recurring Crawls
**Description:** As an SDR, I want to schedule crawl jobs to run on a recurring basis so my lead pipeline stays fresh without manual effort.

**Acceptance Criteria:**
- [ ] User can set a crawl job to repeat: daily, weekly, or monthly
- [ ] Scheduled jobs visible in crawl management UI with next run time
- [ ] User can pause, resume, or delete scheduled jobs
- [ ] Recurring crawls deduplicate against existing data
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

### US-012: User Authentication and Access Control
**Description:** As a Sales Manager, I want team members to log in with their own accounts so I can track who collected what and control access.

**Acceptance Criteria:**
- [ ] Login page with email/password authentication
- [ ] Two roles: Admin (full access) and Team Member (can crawl and view leads, cannot manage users or retention policies)
- [ ] Per-user activity tracking: crawl jobs created, leads exported
- [ ] Admin can create, edit, and deactivate user accounts
- [ ] Typecheck passes
- [ ] Verify in browser using dev-browser skill

## Functional Requirements

- FR-1: The system must accept one or more target URLs/domains and create a crawl job that discovers linked pages up to a configurable depth
- FR-2: The system must respect robots.txt directives and never crawl disallowed pages
- FR-3: The system must throttle requests with configurable rate limits (default: 1 request/second per domain)
- FR-4: The system must extract structured contact fields (name, surname, position, email, phone, company, department, profile URLs) from crawled HTML pages
- FR-5: The system must validate email addresses for format correctness and domain MX record existence
- FR-6: The system must normalize phone numbers to international format using libphonenumber
- FR-7: The system must discard records missing both email and phone, or missing a name
- FR-8: The system must flag low-confidence extractions for manual review
- FR-9: The system must deduplicate leads using fuzzy matching on name, email, and company before database insertion
- FR-10: The system must assign a quality score (0-100) to each lead based on completeness, email validity, source reliability, and recency
- FR-11: The system must log source URL, crawl timestamp, and collection method for every collected record
- FR-12: The system must enforce configurable data retention policies with automatic archival or deletion
- FR-13: The system must maintain an opt-out list of domains and individuals that are never re-crawled
- FR-14: The system must provide a paginated, sortable, filterable lead table in the web dashboard
- FR-15: The system must support full-text search across all lead fields
- FR-16: The system must allow CSV export of selected leads or filtered results
- FR-17: The system must log all export actions (who, when, how many records)
- FR-18: The system must support recurring crawl schedules (daily, weekly, monthly)
- FR-19: The system must provide real-time crawl progress updates in the UI
- FR-20: The system must support user authentication with role-based access control (Admin, Team Member)
- FR-21: The system must handle JavaScript-rendered pages using headless browser (Playwright) when standard HTTP requests fail to extract data
- FR-22: The system must support configurable source types: company websites, business directories, LinkedIn profiles, and custom URLs

## Non-Goals

- No automatic outreach or email sending -- this is a data collection tool, not an outreach platform
- No CRM integration in MVP -- leads are exported as CSV only
- No AI-powered lead enrichment from third-party data providers (e.g., Clearbit, ZoomInfo)
- No mobile app -- web dashboard only
- No real-time notifications or alerts (e.g., "new high-quality lead found")
- No multi-tenant architecture -- single organization deployment
- No custom extraction rule builder in the UI -- extraction logic is code-configured
- No dark web or paid-source crawling -- public web sources only

## Design Considerations

- The dashboard must be usable by non-technical sales team members -- no command-line interaction required
- Lead table is the primary view and must load fast with thousands of records (server-side pagination)
- Crawl management should feel like a simple job scheduler, not a developer tool
- Use shadcn/ui components for a clean, professional look consistent with modern B2B SaaS tools
- Lead detail view should surface audit/compliance info without cluttering the primary contact data
- Quality score should be visually intuitive (color-coded badge or progress bar)

## Technical Considerations

- **Backend:** C# / .NET 8, ASP.NET Core Web API, Entity Framework Core 8, SQL Server
- **Crawling:** HtmlAgilityPack + HttpClient for static pages, Playwright (.NET) for JS-rendered pages
- **Background Jobs:** Hangfire with SQL Server persistence for crawl job execution and scheduling
- **Frontend:** React 18+ (Vite), TypeScript, React Router v6, shadcn/ui, Tailwind CSS, TanStack Table
- **Auth:** ASP.NET Core Identity + JWT Bearer tokens
- **Rate Limiting:** Custom HttpClient delegating handler with per-domain throttling
- **robots.txt:** Parsed and cached per domain before any crawl requests are made
- **LinkedIn caveat:** LinkedIn actively blocks automated access. The crawler should handle 429/403 responses gracefully, respect rate limits strictly, and warn users that LinkedIn yields may be limited. Consider LinkedIn as a "best effort" source type.
- **SQL Server full-text indexing** should be used for the lead search feature (FR-15)
- **Hangfire Dashboard** provides built-in job monitoring but should be restricted to Admin role

## Success Metrics

- Sales team spends less than 5 minutes per day on lead research (down from 2-3 hours)
- 90%+ of extracted leads have valid email addresses after validation
- Zero compliance incidents -- all collected data has a documented source and audit trail
- Lead database contains fewer than 5% duplicate records
- Sales team can go from "enter a URL" to "export leads CSV" in under 10 minutes
- Dashboard loads lead table with 10,000+ records in under 2 seconds

## Open Questions

- Should the system attempt to detect and skip personal/non-business email addresses (e.g., gmail.com, yahoo.com)?
- What is the maximum crawl depth that makes sense before results become irrelevant?
- Should there be a global daily crawl limit to manage server resources?
- How should the system handle pages behind login walls -- skip silently or report as "access denied"?
- Should the opt-out list support wildcard patterns (e.g., *.gov.za)?
- What is the data retention default -- 90 days, 1 year, indefinite until manual deletion?
