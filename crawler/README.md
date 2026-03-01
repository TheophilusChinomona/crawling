# LeadCrawl Crawler

Standalone web crawler (Crawlee). Use for any URL or documentation crawling; can be driven by a research agent or the LeadCrawl .NET backend. Discovers links, fetches pages (HTTP or headless browser), and outputs markdown plus minimal lead-shaped data for pipelines or backend ingestion.

## Requirements

- Python 3.10+
- pip

## Installation

From the `crawler/` directory:

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

# Install the package (Crawlee with playwright + beautifulsoup is in pyproject.toml)
pip install -e .

# Install Playwright browsers (required for JS-rendered pages)
playwright install
```

For headless Chromium only:

```bash
playwright install chromium
```

## Running the crawler

Default run (starts at https://crawlee.dev, max 10 requests, HTTP/BeautifulSoup):

```bash
python -m leadcrawl_crawler
```

### Configuration via environment

| Variable | Description | Default |
|----------|-------------|---------|
| `LEADCRAWL_START_URLS` | Comma-separated start URLs | `https://crawlee.dev` |
| `LEADCRAWL_MAX_REQUESTS` | Maximum pages to crawl per run | `10` |
| `LEADCRAWL_USE_PLAYWRIGHT` | Set to `1`, `true`, or `yes` to use headless browser | (off) |
| `LEADCRAWL_INCLUDE_GLOBS` | Comma-separated glob patterns; only matching URLs are enqueued (e.g. `https://openrouter.ai/docs/**`) | (none) |

Example:

```bash
set LEADCRAWL_START_URLS=https://example.com,https://example.org
set LEADCRAWL_MAX_REQUESTS=50
python -m leadcrawl_crawler
```

You can also pass start URLs as arguments (overrides env):

```bash
python -m leadcrawl_crawler https://news.ycombinator.com/jobs
python -m leadcrawl_crawler https://example.com/jobs https://example.com/careers
```

### Testing on job listings

To try the crawler on job-listing-style pages, use **public sites that allow or tolerate crawling**. Do **not** target LinkedIn, Indeed, Glassdoor, or similar: their Terms of Service prohibit scraping and they use strong anti-bot measures (blocks, bans, legal risk).

**Safe options for a quick test:**

- **Hacker News Jobs** (static HTML, same-domain links):
  ```bash
  python -m leadcrawl_crawler https://news.ycombinator.com/jobs
  ```
- Any **company career page** or **public job board** that permits bots (check `robots.txt` and the site’s terms before crawling at scale).

Keep `LEADCRAWL_MAX_REQUESTS` low (e.g. 10–20) when testing to avoid hammering the server.

### Output

Crawlee writes to a `storage/` directory (by default under the current working directory):

- **Dataset** (`storage/datasets/default/`): JSONL records with `url`, `title`, and placeholder fields for lead data (`name`, `email`, `position`, etc.) for the .NET pipeline to validate and store.
- **Markdown** (`storage/key_value_stores/default/`): Each crawled page is also saved as markdown (one file per URL, keyed by a hash of the URL with a `.md` extension). The file starts with `Source: <url>` for traceability. Use these for full-page text content, RAG, or archival.

## Integration with .NET

The crawler is intended to be run by the LeadCrawl .NET backend (e.g. via Hangfire or the API):

1. **On-demand:** Invoke `python -m leadcrawl_crawler` (or the installed `leadcrawl_crawler` module) with the desired working directory and env (e.g. `LEADCRAWL_START_URLS`, `LEADCRAWL_MAX_REQUESTS`). After the run, read the output from Crawlee storage (e.g. `storage/datasets/default/`) and push records into SQL Server / validation pipeline.

2. **Later:** The crawler can be extended to POST results directly to a .NET API endpoint or push to a queue (e.g. Redis) for async processing.

Do not commit `storage/`, `.venv/`, or `__pycache__/` (see `.gitignore`).

### Crawling documentation sites (e.g. OpenRouter docs)

To crawl only doc pages and export to a path-based folder:

1. Set `LEADCRAWL_INCLUDE_GLOBS` to restrict links (e.g. `https://openrouter.ai/docs/**`).
2. Run the crawler with a dedicated `CRAWLEE_STORAGE_DIR` and start URL.
3. Run the export script to turn hashed markdown files into a path-mirrored folder:

```bash
# From crawler/
export CRAWLEE_STORAGE_DIR="../storage-openrouter-docs"
export LEADCRAWL_START_URLS="https://openrouter.ai/docs/quickstart"
export LEADCRAWL_MAX_REQUESTS=150
export LEADCRAWL_INCLUDE_GLOBS="https://openrouter.ai/docs/**"
python -m leadcrawl_crawler https://openrouter.ai/docs/quickstart

python scripts/export_docs_to_structured_folder.py \
  ../storage-openrouter-docs/key_value_stores/default \
  ../docs-crawl/openrouter-docs \
  --url-prefix "https://openrouter.ai/docs/"
```

Output: `docs-crawl/openrouter-docs/` with one `.md` per doc page (e.g. `quickstart.md`, `api/reference/overview.md`) and a `README.md` index.
