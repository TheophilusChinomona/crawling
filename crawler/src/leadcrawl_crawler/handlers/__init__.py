"""Crawlee request handlers for LeadCrawl."""

from leadcrawl_crawler.handlers.default import handle_beautifulsoup, handle_playwright

__all__ = ["handle_beautifulsoup", "handle_playwright"]
