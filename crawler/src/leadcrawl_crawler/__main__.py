"""Entrypoint: python -m leadcrawl_crawler [URL1 [URL2 ...]]."""

from __future__ import annotations

import sys

from leadcrawl_crawler.runner import main_sync

if __name__ == "__main__":
    # Optional: pass start URLs as arguments (overrides LEADCRAWL_START_URLS)
    urls = [a for a in sys.argv[1:] if a.strip()] if len(sys.argv) > 1 else None
    main_sync(urls=urls)
