# Product Roadmap

1. [ ] **Database Schema & Lead Model** -- Design and implement the SQL Server database schema for leads (name, surname, position, email, phone, company, department, profile URLs), crawl jobs, audit logs, and deduplication indexes. Include EF Core migrations. `S`
2. [ ] **Core Crawling Engine** -- Build the web crawler that accepts a target URL or domain, discovers linked pages, and extracts raw HTML content. Implement request throttling, robots.txt compliance, user-agent configuration, and retry logic. `M`
3. [ ] **Data Extraction Pipeline** -- Implement structured data extraction from crawled pages using CSS selectors, regex patterns, and heuristics to identify and pull contact fields (name, email, phone, position, company, department, LinkedIn URLs) from common page layouts like team pages and about pages. `L`
4. [ ] **Smart Filtering & Validation** -- Add a validation layer that checks email format and domain validity, normalizes phone numbers to international format, classifies job titles into departments, discards incomplete or irrelevant records, and flags low-confidence extractions for manual review. `M`
5. [ ] **Deduplication Engine** -- Implement fuzzy matching across name, email, and company fields to detect and merge duplicate leads. New crawl results are compared against existing database records before insertion. `S`
6. [ ] **Compliance & Audit Logging** -- Record source URL, crawl timestamp, and collection method for every lead. Implement configurable data retention policies with automatic archival/deletion. Add opt-out list support so flagged domains or individuals are never re-crawled. `M`
7. [ ] **Backend API** -- Build a REST API (ASP.NET Core Web API) exposing endpoints for: managing crawl jobs (create, pause, resume, delete), browsing and searching leads with filters, viewing audit logs, exporting leads as CSV, and managing crawl configuration (target domains, schedules, rate limits). `M`
8. [ ] **Lead Dashboard (Frontend)** -- Build a web UI where sales team members can browse leads in a searchable, filterable table; view lead detail including source and audit info; and export selected leads as CSV. `L`
9. [ ] **Crawl Management UI** -- Add frontend pages for creating new crawl jobs (enter target domains/URLs), viewing crawl progress in real time, scheduling recurring crawls, and adjusting rate-limiting settings. `M`
10. [ ] **Lead Scoring** -- Assign a quality score (0-100) to each lead based on data completeness, source reliability, email verification status, and recency. Display scores in the dashboard and allow sorting/filtering by score. `S`
11. [ ] **CRM Export Integration** -- Add the ability to push selected leads directly to a CRM (HubSpot or Salesforce) via API, mapping LeadCrawl fields to CRM contact fields. Include a settings page for API key configuration. `M`
12. [ ] **User Authentication & Team Management** -- Add login, role-based access (admin vs. team member), and per-user crawl activity tracking so managers can see who collected what. `M`

> Notes
> - Items are ordered by technical dependency: database first, then crawler, then extraction, then validation, then the API and UI layers on top.
> - Items 1-6 form the backend foundation. Items 7-9 deliver the usable product. Items 10-12 are enhancements.
> - The MVP is items 1 through 9 -- a working crawler with validation, compliance logging, and a usable dashboard.
> - Effort estimates assume a single developer. XS = 1 day, S = 2-3 days, M = 1 week, L = 2 weeks, XL = 3+ weeks.
