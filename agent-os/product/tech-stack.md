# Tech Stack

## Backend -- Web API & Crawling Engine

| Component | Technology | Purpose |
|---|---|---|
| Language | **C# / .NET 8** | Primary language for the Web API, crawling engine, and data pipeline |
| Web API | **ASP.NET Core Web API** | REST API serving the frontend, with Swagger/OpenAPI docs, async support, and model validation |
| Web Crawling | **HtmlAgilityPack** + **HttpClient** | HTTP requests and HTML parsing for crawling public web pages |
| Browser Rendering | **Playwright** (.NET) | Headless browser for JavaScript-rendered pages (SPAs, dynamically loaded team directories) |
| Background Jobs | **Hangfire** | Background job processing for crawl jobs, deduplication, and scheduled/recurring tasks |
| Data Validation | **FluentValidation** | Schema validation and normalization for extracted lead data |
| Email Validation | **MailKit** / custom MX checks | Format validation and domain MX record verification for extracted emails |
| Phone Normalization | **libphonenumber-csharp** | Parse and normalize phone numbers to international format |
| Fuzzy Matching | **FuzzySharp** | Deduplication via fuzzy string matching on name, email, and company fields |
| ORM | **Entity Framework Core 8** | Database access, LINQ queries, and schema migrations |

## Frontend -- Sales Dashboard

| Component | Technology | Purpose |
|---|---|---|
| Framework | **React 18+** (Vite) | Component-based SPA framework for building the sales dashboard |
| Language | **TypeScript** | Type safety across the frontend codebase |
| Routing | **React Router v6** | Client-side routing for the SPA |
| UI Components | **shadcn/ui** + **Tailwind CSS** | Pre-built accessible components and utility-first styling for rapid UI development |
| Data Tables | **TanStack Table** | Filterable, sortable, paginated lead table with column controls |
| HTTP Client | **Axios** or **fetch** | API communication with the .NET backend |
| Forms | **React Hook Form** + **Zod** | Form handling and client-side validation for crawl job configuration and settings |
| State Management | **React Context** / **Zustand** | Lightweight client-side state for UI state and cached data |

## Database & Storage

| Component | Technology | Purpose |
|---|---|---|
| Primary Database | **SQL Server** | Relational storage for leads, crawl jobs, audit logs, users, and configuration |
| ORM / Migrations | **Entity Framework Core 8** | Code-first migrations and LINQ-based data access |
| Cache / Broker | **Redis** | Hangfire state caching, rate-limit counters, and optional distributed cache |
| File Storage | **Local filesystem** (MVP) | Temporary storage for raw crawl output and CSV exports |

## Infrastructure & DevOps

| Component | Technology | Purpose |
|---|---|---|
| Containerization | **Docker** + **Docker Compose** | Local development environment and production deployment |
| Web Server | **Kestrel** (built-in) | ASP.NET Core's built-in high-performance web server |
| Environment Config | **appsettings.json** + **User Secrets** | Configuration and secrets management following .NET conventions |
| Linting / Formatting | **dotnet format** + **StyleCop Analyzers** | C# code quality and formatting |
| Frontend Linting | **ESLint** + **Prettier** | TypeScript/React code quality |

## Compliance & Security

| Component | Technology | Purpose |
|---|---|---|
| robots.txt Parsing | **RobotsTxtParser** (NuGet) | Respect for robots.txt directives before crawling |
| Audit Logging | **Custom middleware** (SQL Server-backed) | Record source URL, timestamp, and method for every collected record |
| Rate Limiting | **Custom HttpClient handler** + **Redis counters** | Prevent aggressive crawling and IP bans |
| Authentication | **ASP.NET Core Identity** + **JWT Bearer** | User login, session management, and role-based access control |
| Secrets Management | **User Secrets** (dev) / **Environment variables** (prod) | API keys, database credentials, and CRM tokens kept out of code |

## Key Architectural Decisions

- **ASP.NET Core Web API over FastAPI/Django:** The team works in .NET, so using ASP.NET Core keeps the entire backend in a single ecosystem with strong tooling, middleware pipeline, and Entity Framework integration.
- **HtmlAgilityPack over Scrapy:** HtmlAgilityPack is the standard .NET library for HTML parsing. Combined with HttpClient, it provides full control over crawl logic within C#.
- **Playwright as a supplement, not primary:** Most target pages (company team pages, directories) serve static HTML. Playwright is reserved for JavaScript-heavy pages that HttpClient alone cannot render.
- **Entity Framework Core over Dapper:** EF Core provides code-first migrations, change tracking, and LINQ queries that accelerate development. Dapper can be introduced later for performance-critical read queries if needed.
- **SQL Server over PostgreSQL:** Aligns with the team's existing database expertise and tooling (SSMS, Azure SQL compatibility).
- **Hangfire for background jobs:** Provides a dashboard UI, retry logic, scheduled jobs, and SQL Server-backed persistence out of the box -- no separate message broker required for MVP.
- **React (Vite) over Next.js:** The frontend is a client-side SPA — no server-side rendering needed. Vite provides fast dev builds and HMR. React Router handles client-side navigation. This keeps the frontend simple and decoupled from the .NET backend.
