# Research agent tools

This repo includes two **standalone, independent** tools for research agents: a web crawler and a PDF-to-markdown converter. They have no code dependency on each other; you can use one or both.

## Tools

| Tool | Purpose | Entrypoint | Full docs |
|------|---------|------------|-----------|
| **Web crawler** | Crawl websites or documentation; discover links; save pages as markdown + JSONL | `python -m leadcrawl_crawler [URLs...]` from repo root (after `pip install -e crawler/`) | [crawler/README.md](crawler/README.md) |
| **PDF to markdown** | Convert PDFs to markdown (local PyMuPDF, OCR, or vision-parse) | `python pdf2markdown/convert.py <file-or-dir> [options]` from repo root (after `pip install -r pdf2markdown/requirements.txt`) | [pdf2markdown/README.md](pdf2markdown/README.md) |

## Project skills

Cursor project skills document when and how to invoke each tool so an agent can use them without coupling:

- **[.cursor/skills/web-crawler](.cursor/skills/web-crawler)** — When to crawl, env vars, output paths, optional docs-export and models scripts.
- **[.cursor/skills/pdf2markdown](.cursor/skills/pdf2markdown)** — When to convert PDFs, modes (local, vision, by-question), env vars, output.

These skills can be given to a research agent or turned into reusable skills in other projects.

## Output format

Both tools emit markdown with a **`Source:`** header (URL or file path) so you can combine crawler output and PDF output in the same pipeline or index.
