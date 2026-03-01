"""
Export Crawlee key-value store markdown files to a path-based folder structure.

Reads .md files from a Crawlee key_value_stores/default directory (each file
starts with "Source: <url>"), filters by URL prefix, and writes them under
output_dir mirroring the URL path (e.g. .../docs/guides/foo -> guides/foo.md).

Usage:
  python export_docs_to_structured_folder.py <kvs_dir> <output_dir> [--url-prefix PREFIX]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


SOURCE_LINE_PATTERN = re.compile(r"^Source:\s*(.+)\s*$")


def _extract_url_from_markdown(content: str) -> str | None:
    """Extract URL from first line 'Source: <url>'."""
    first_line = content.split("\n", 1)[0].strip()
    m = SOURCE_LINE_PATTERN.match(first_line)
    return m.group(1).strip() if m else None


def _url_path_to_file_path(url: str, url_prefix: str) -> str | None:
    """
    Map URL to relative file path under output dir.
    e.g. https://openrouter.ai/docs/quickstart -> quickstart.md
         https://openrouter.ai/docs/guides/foo -> guides/foo.md
    """
    prefix = url_prefix.rstrip("/")
    if not url.startswith(prefix + "/") and url != prefix:
        return None
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    prefix_parsed = urlparse(url_prefix)
    prefix_path = prefix_parsed.path.rstrip("/") or "/"
    if path.startswith(prefix_path + "/"):
        path = path[len(prefix_path) + 1 :]
    elif path == prefix_path or not path:
        path = "index"
    # Sanitize: only allow alphanumeric, hyphen, underscore, slash
    parts = []
    for segment in path.split("/"):
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in segment)
        if safe:
            parts.append(safe)
    if not parts:
        parts.append("index")
    return "/".join(parts) + ".md"


def export_docs_to_structured_folder(
    kvs_dir: Path,
    output_dir: Path,
    url_prefix: str = "https://openrouter.ai/docs/",
) -> list[tuple[str, Path]]:
    """
    Read .md files from kvs_dir, filter by url_prefix, write to output_dir by path.
    Returns list of (url, output_file_path) for the written files.
    """
    if not kvs_dir.is_dir():
        raise NotADirectoryError(f"Key-value store dir is not a directory: {kvs_dir}")

    output_dir = output_dir.resolve()
    written: list[tuple[str, Path]] = []

    for md_file in kvs_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8", errors="replace")
        url = _extract_url_from_markdown(content)
        if not url:
            continue
        rel_path = _url_path_to_file_path(url, url_prefix)
        if rel_path is None:
            continue
        out_path = output_dir / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
        written.append((url, out_path))

    return written


def _write_index(output_dir: Path, entries: list[tuple[str, Path]]) -> None:
    """Write README.md with a list of all pages and relative links."""
    lines = [
        "# OpenRouter docs (crawled)",
        "",
        "Local mirror of [OpenRouter documentation](https://openrouter.ai/docs).",
        "",
        "## Pages",
        "",
    ]
    for url, out_path in sorted(entries, key=lambda x: str(x[1]).replace("\\", "/")):
        rel = out_path.relative_to(output_dir)
        link = str(rel).replace("\\", "/")
        lines.append(f"- [{link}]({link}) — {url}")
    (output_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export Crawlee KVS markdown to path-based folder (e.g. for OpenRouter docs)."
    )
    parser.add_argument(
        "kvs_dir",
        type=Path,
        help="Path to Crawlee key_value_stores/default directory",
    )
    parser.add_argument(
        "output_dir",
        type=Path,
        help="Output directory for structured .md files",
    )
    parser.add_argument(
        "--url-prefix",
        default="https://openrouter.ai/docs/",
        help="Only export URLs under this prefix (default: https://openrouter.ai/docs/)",
    )
    parser.add_argument(
        "--no-index",
        action="store_true",
        help="Do not write README.md index",
    )
    args = parser.parse_args()

    try:
        written = export_docs_to_structured_folder(
            args.kvs_dir.resolve(),
            args.output_dir.resolve(),
            url_prefix=args.url_prefix,
        )
    except NotADirectoryError as e:
        print(str(e), file=sys.stderr)
        return 1

    if not written:
        print("No matching markdown files found.", file=sys.stderr)
        return 0

    if not args.no_index:
        _write_index(args.output_dir.resolve(), written)

    print(f"Exported {len(written)} pages to {args.output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
