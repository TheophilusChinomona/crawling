"""Run the LeadCrawl crawler with configurable URLs and crawler type."""

from __future__ import annotations

import os
import asyncio
from typing import Sequence

from leadcrawl_crawler.handlers.default import handle_beautifulsoup, handle_playwright


def _get_config() -> tuple[list[str], int, bool]:
    """Read config from environment with defaults."""
    urls_str = os.environ.get("LEADCRAWL_START_URLS", "https://crawlee.dev")
    urls = [u.strip() for u in urls_str.split(",") if u.strip()]
    max_requests = int(os.environ.get("LEADCRAWL_MAX_REQUESTS", "10"))
    use_playwright = os.environ.get("LEADCRAWL_USE_PLAYWRIGHT", "").lower() in ("1", "true", "yes")
    return urls, max_requests, use_playwright


async def run(
    urls: Sequence[str] | None = None,
    max_requests_per_crawl: int = 10,
    use_playwright: bool = False,
) -> None:
    """
    Run the crawler on the given URLs.

    Args:
        urls: Start URLs. If None, uses LEADCRAWL_START_URLS env (comma-separated).
        max_requests_per_crawl: Max pages to crawl. Default 10.
        use_playwright: If True, use PlaywrightCrawler (JS rendering); else BeautifulSoupCrawler.
    """
    if urls is None:
        env_urls, env_max, env_playwright = _get_config()
        urls = env_urls
        max_requests_per_crawl = env_max
        use_playwright = env_playwright
    else:
        _, env_max, env_playwright = _get_config()
        max_requests_per_crawl = env_max
        use_playwright = env_playwright

    if not urls:
        raise ValueError("At least one start URL is required")

    if use_playwright:
        from crawlee.crawlers import PlaywrightCrawler

        crawler = PlaywrightCrawler(max_requests_per_crawl=max_requests_per_crawl)
        crawler.router.default_handler(handle_playwright)
    else:
        from crawlee.crawlers import BeautifulSoupCrawler

        crawler = BeautifulSoupCrawler(max_requests_per_crawl=max_requests_per_crawl)
        crawler.router.default_handler(handle_beautifulsoup)

    await crawler.run(list(urls))


def main_sync(
    urls: Sequence[str] | None = None,
    max_requests_per_crawl: int = 10,
    use_playwright: bool = False,
) -> None:
    """Synchronous entrypoint that runs the async crawler."""
    asyncio.run(run(urls=urls, max_requests_per_crawl=max_requests_per_crawl, use_playwright=use_playwright))
