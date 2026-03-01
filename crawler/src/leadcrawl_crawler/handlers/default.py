"""Default request handler: extract minimal lead-shaped data and enqueue links."""

from __future__ import annotations

import hashlib
import os
from typing import TYPE_CHECKING

from crawlee import Glob
from markdownify import markdownify as md

if TYPE_CHECKING:
    from crawlee.crawlers import BeautifulSoupCrawlingContext, PlaywrightCrawlingContext


def _get_include_globs() -> list[str]:
    """Read LEADCRAWL_INCLUDE_GLOBS env (comma-separated); return non-empty list or empty."""
    raw = os.environ.get("LEADCRAWL_INCLUDE_GLOBS", "").strip()
    if not raw:
        return []
    return [g.strip() for g in raw.split(",") if g.strip()]


def _html_to_markdown(html: str, url: str) -> str:
    """Convert HTML to markdown and prepend source URL."""
    body_md = md(html) or ""
    return f"Source: {url}\n\n{body_md}"


def _markdown_key(url: str) -> str:
    """Return a filesystem-safe key for the markdown file (one per URL)."""
    h = hashlib.sha256(url.encode()).hexdigest()[:16]
    return f"{h}.md"


async def _save_markdown(context: "BeautifulSoupCrawlingContext | PlaywrightCrawlingContext", html: str, url: str) -> None:
    """Save page content as markdown to the default key-value store."""
    markdown = _html_to_markdown(html, url)
    key = _markdown_key(url)
    kvs = await context.get_key_value_store()
    await kvs.set_value(key, markdown, content_type="text/markdown")


async def handle_beautifulsoup(context: "BeautifulSoupCrawlingContext") -> None:
    """Handle a page with BeautifulSoup context: extract title/URL, push data, save markdown, enqueue links."""
    url = context.request.url
    title = context.soup.title.string if context.soup and context.soup.title else ""
    context.log.info("Processing %s ...", url)

    html = str(context.soup) if context.soup else ""
    await _save_markdown(context, html, url)

    data = {
        "url": url,
        "title": title,
        "name": None,
        "surname": None,
        "position": None,
        "email": None,
        "phone": None,
        "company": None,
        "department": None,
        "profile_url": None,
    }
    await context.push_data(data)
    globs = _get_include_globs()
    if globs:
        await context.enqueue_links(strategy="same-domain", include=[Glob(g) for g in globs])
    else:
        await context.enqueue_links(strategy="same-domain")


async def handle_playwright(context: "PlaywrightCrawlingContext") -> None:
    """Handle a page with Playwright context: extract title/URL, push data, save markdown, enqueue links."""
    url = context.request.url
    title = await context.page.title() if context.page else ""
    context.log.info("Processing %s ...", url)

    html = await context.page.content() if context.page else ""
    await _save_markdown(context, html, url)

    data = {
        "url": url,
        "title": title,
        "name": None,
        "surname": None,
        "position": None,
        "email": None,
        "phone": None,
        "company": None,
        "department": None,
        "profile_url": None,
    }
    await context.push_data(data)
    globs = _get_include_globs()
    if globs:
        await context.enqueue_links(strategy="same-domain", include=[Glob(g) for g in globs])
    else:
        await context.enqueue_links(strategy="same-domain")
