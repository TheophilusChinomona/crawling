# pdf2markdown

Standalone tool to convert local PDFs to markdown. By default it tries **local extraction** with [PyMuPDF](https://github.com/pymupdf/PyMuPDF) first (no API key); if that yields no text, it falls back to [vision-parse](https://github.com/iamarunbrahma/vision-parse) (Vision LLMs). Output includes a `Source: <path>` header for traceability.

## Prerequisites

- Python 3.9+
- **PyMuPDF** (`pymupdf`) is required for local extraction (included in `requirements.txt`).
- For the vision-parse fallback: **Ollama** with a vision model (e.g. `llama3.2-vision:11b`) or an **OpenAI** / **Google Gemini** API key.

## Installation

From the repo root or from inside `pdf2markdown/`:

```bash
pip install -r pdf2markdown/requirements.txt
```

This installs PyMuPDF (local extraction) and vision-parse with API extras (fallback). For vision-parse only without API extras:

```bash
pip install vision-parse
```

## Environment variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PDF2MD_MODEL` | Vision model name | `llama3.2-vision:11b` |
| `PDF2MD_TEMPERATURE` | Model temperature | `0.4` |
| `PDF2MD_TOP_P` | Model top_p | `0.5` |
| `PDF2MD_IMAGE_MODE` | Image mode: `url` or `base64` | `base64` |
| `OPENAI_API_KEY` | Required for OpenAI models (e.g. gpt-4o) | — |
| `GOOGLE_API_KEY` or `GEMINI_API_KEY` | Required for Gemini models | — |
| `PDF2MD_VISION_MAX_RETRIES` | Max retries for vision-parse API calls on transient errors (500, 429, 503, timeout) | `3` |
| `PDF2MD_VISION_RETRY_BACKOFF_SEC` | Base delay in seconds for exponential backoff between retries | `5` |
| `PDF2MD_OCR_LANG` | Tesseract language(s) for local OCR (e.g. `eng`, `eng+afr`) | `eng` |
| `TESSDATA_PREFIX` | Path to Tesseract tessdata folder (required for OCR if not auto-detected) | — |

Ollama does not require an API key; set `PDF2MD_MODEL` to an Ollama vision model (e.g. `llama3.2-vision:11b`).

When using vision-parse (e.g. `--vision` or fallback after local extraction), the script retries on **transient** API errors (500, 429, 503, timeouts). Non-transient errors (invalid API key, model not found) fail immediately. Set `PDF2MD_VISION_MAX_RETRIES=0` to disable retries.

### Local extraction (PyMuPDF)

By default the script tries **local extraction** first using PyMuPDF: it extracts text from each page with no API key or network. If that yields at least some text, that result is used and written in the same format (`Source:` header and `--- Page N ---` separators). If local extraction fails or returns only empty pages, the script falls back to vision-parse (unless you passed `--local`).

- **`--local`** — Use only local extraction (PyMuPDF). Do not call vision-parse. Exits with an error if no text could be extracted (e.g. image-only PDF).
- **`--vision`** — Skip local extraction and use only vision-parse (Vision LLM). Requires API key or Ollama for the chosen model.
- **`--strip-header`** — Remove common SA Exam Papers boilerplate from the first page (text up to and including `www.saexampapers.co.za`). Use for exam PDFs from that source.
- **`--rich`** — Use **pymupdf4llm** for local extraction when available: produces markdown tables and better structure. Single-file or batch. Requires `pip install pymupdf4llm`; if not installed, falls back to plain PyMuPDF extraction.

### Local OCR (Tesseract)

When local text extraction returns no or very little text (e.g. scanned or image-heavy PDFs), the script can use **local OCR** via [Tesseract](https://github.com/tesseract-ocr/tesseract) and PyMuPDF’s integrated OCR. No new Python packages are required; you must install the **Tesseract** engine and language data on your system (e.g. [Windows](https://github.com/UB-Mannheim/tesseract/wiki), or `apt install tesseract-ocr tesseract-ocr-eng` on Linux). Set **`TESSDATA_PREFIX`** to the tessdata folder (e.g. `C:\Program Files\Tesseract-OCR\tessdata` on Windows, `/usr/share/tesseract-ocr/4.00/tessdata` on Unix) if PyMuPDF does not find it automatically.

- **Auto-OCR:** If normal extraction yields fewer than ~50 characters, the script tries OCR once; if that returns text, it is used and written as markdown. If OCR fails or returns nothing and you did not pass `--local`, the script falls back to vision-parse.
- **`--ocr`** — Use **only** local OCR (skip normal text extraction). Good for scanned PDFs. If OCR fails and you passed `--local`, the script exits with an error; otherwise it falls back to vision-parse.
- **`--ocr-language`** — Tesseract language(s), e.g. `eng` or `eng+afr` for English and Afrikaans (default: env `PDF2MD_OCR_LANG` or `eng`).
- **`--ocr-dpi`** — Resolution used for OCR (default: 300).

### Question-linked extraction (pdfplumber)

For complex exam or question-based PDFs, use **`--by-question`** to segment content by question headers, crop each region, and output markdown with **`## Question N`** sections. Text and tables are extracted per question. By default, region PNGs are **not** written, so you get editable text/markdown only and avoid redundant “images of text”. Single-file only (pass a PDF file, not a directory).

- **`--by-question`** — Use [pdfplumber](https://github.com/jsvine/pdfplumber) to detect question headers (e.g. `1.1`, `QUESTION 1`, `Vraag 1`, `SOURCE 1A`), assign content to questions by position, crop per region, and write markdown with `## Question 1.1`, `## Question 1.2`, etc. Requires `pdfplumber` (included in `requirements.txt`).
- **`--images`** — With `--by-question`: write per-question region PNGs to `*_assets/` and link them in the markdown (e.g. for diagrams or figures). Off by default.
- **`--no-images`** — With `--by-question`: same as default (no region PNGs). Kept for backwards compatibility.

Question detection is heuristic and tuned for common SA exam/memo formats; other languages or layouts may need tuning. If no question headers are found, the script falls back to one `## Page N` section per page.

### Quick start with Gemini

If you have a [Gemini API key](https://aistudio.google.com/app/apikey), the script **auto-discovers** which Gemini models your key can use and accepts any of them (e.g. `gemini-2.0-flash`, `gemini-2.5-flash`). You can pass the model name with or without the `models/` prefix. If the model you request is not available, the script exits with an error that lists example models you can use.

```bash
# Set your key (use GEMINI_API_KEY or GOOGLE_API_KEY)
set GEMINI_API_KEY=your-key-here

# Use any Gemini model your key supports (e.g. gemini-2.0-flash)
set PDF2MD_MODEL=gemini-2.0-flash
python pdf2markdown/convert.py path/to/document.pdf --output document.md

# Or pass the model on the command line
python pdf2markdown/convert.py path/to/document.pdf --model gemini-2.0-flash --output document.md
```

On Linux/macOS use `export GEMINI_API_KEY=your-key-here` and `export PDF2MD_MODEL=gemini-2.0-flash` (or another model from the discovery list) instead of `set`.

Optional: copy `pdf2markdown/.env.example` to `pdf2markdown/.env`, add your key, then load it before running (e.g. `set -a && source pdf2markdown/.env && set +a` on bash, or use your IDE’s env support). Do not commit `.env`.

## Usage

```bash
# Output to <filename>.md next to the PDF (default)
python pdf2markdown/convert.py path/to/document.pdf

# Output to a specific file
python pdf2markdown/convert.py path/to/document.pdf --output out.md

# Print markdown to stdout
python pdf2markdown/convert.py path/to/document.pdf --output -

# Override model (env or CLI) when using vision-parse
python pdf2markdown/convert.py document.pdf --model gpt-4o
python pdf2markdown/convert.py document.pdf --model gemini-2.0-flash   # or any Gemini model your key supports

# Local extraction only (no API key)
python pdf2markdown/convert.py document.pdf --local

# Local OCR only (scanned PDFs; requires Tesseract and TESSDATA_PREFIX)
python pdf2markdown/convert.py document.pdf --ocr --local
python pdf2markdown/convert.py document.pdf --ocr --ocr-language eng+afr

# Skip local and use only vision-parse
python pdf2markdown/convert.py document.pdf --vision --output out.md

# Richer local extraction (markdown tables, structure) — requires: pip install pymupdf4llm
python pdf2markdown/convert.py document.pdf --rich

# Strip SA Exam Papers boilerplate from the first page
python pdf2markdown/convert.py document.pdf --strip-header

# Batch: convert all PDFs in a directory (optionally strip header)
python pdf2markdown/convert.py "Pdfs for test/Exams" --local --strip-header

# Question-linked extraction (single file): ## Question 1.1, 1.2, ... with tables (no region images by default)
python pdf2markdown/convert.py path/to/exam.pdf --by-question --output exam.md
python pdf2markdown/convert.py path/to/exam.pdf --by-question --images --output exam.md   # also write *_assets/ PNGs (e.g. for diagrams)
```

Output markdown starts with `Source: <file_uri>` and then the converted content, with `--- Page N ---` between pages (omitted when using `--rich`). With `--by-question`, output uses `## Question N` sections; add `--images` to also write per-question region PNGs to `*_assets/`. The `Source:` header lets you combine this output with other text sources (e.g. crawled pages) in the same pipeline.
