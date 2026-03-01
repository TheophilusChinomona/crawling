#!/usr/bin/env python3
"""Convert a local PDF to markdown. Tries local extraction (PyMuPDF) first, then vision-parse if needed. Output includes Source: <path> header."""

from __future__ import annotations

import argparse
import re
import os
import sys
import time
from pathlib import Path

# Load .env from the script directory so GEMINI_API_KEY etc. are picked up without exporting
_SCRIPT_DIR = Path(__file__).resolve().parent
_env_file = _SCRIPT_DIR / ".env"
if _env_file.exists():
    try:
        from dotenv import load_dotenv
        load_dotenv(_env_file)
    except ImportError:
        pass


def _get_config() -> dict:
    """Read config from environment."""
    model = os.environ.get("PDF2MD_MODEL", "llama3.2-vision:11b")
    temperature = float(os.environ.get("PDF2MD_TEMPERATURE", "0.4"))
    top_p = float(os.environ.get("PDF2MD_TOP_P", "0.5"))
    openai_key = os.environ.get("OPENAI_API_KEY", "")
    google_key = os.environ.get("GOOGLE_API_KEY", "") or os.environ.get("GEMINI_API_KEY", "")
    image_mode = os.environ.get("PDF2MD_IMAGE_MODE", "base64") or None
    if image_mode and image_mode.lower() not in ("url", "base64"):
        image_mode = "base64"
    return {
        "model_name": model,
        "temperature": temperature,
        "top_p": top_p,
        "openai_api_key": openai_key.strip() or None,
        "google_api_key": google_key.strip() or None,
        "image_mode": image_mode,
    }


def _is_ollama_model(model_name: str) -> bool:
    """Heuristic: Ollama models typically contain ':' (e.g. llama3.2-vision:11b)."""
    return ":" in model_name or model_name.startswith("llava") or model_name.startswith("llama")


def _get_api_key(config: dict) -> str | None:
    """Return the appropriate API key for the model, or None for Ollama."""
    model = (config["model_name"] or "").lower()
    if _is_ollama_model(model):
        return None
    if "gpt" in model or "openai" in model:
        return config["openai_api_key"]
    if "gemini" in model:
        return config["google_api_key"]
    return config["openai_api_key"] or config["google_api_key"]


def _normalize_gemini_model_name(name: str) -> str:
    """Return model name without 'models/' prefix for matching."""
    s = (name or "").strip()
    if s.startswith("models/"):
        return s[7:]
    return s


def _list_accessible_gemini_models(api_key: str) -> set[str]:
    """Return set of Gemini model names that support generateContent (full 'models/...' form)."""
    try:
        import google.generativeai as genai
    except ImportError:
        return set()
    genai.configure(api_key=api_key)
    out = set()
    for m in genai.list_models():
        name = getattr(m, "name", None) or ""
        methods = getattr(m, "supported_generation_methods", []) or []
        if "generateContent" in methods and "gemini" in name.lower():
            out.add(name)
    return out


def _resolve_gemini_model(
    requested: str, api_key: str
) -> tuple[str, str] | None:
    """
    Resolve user-provided model name to an accessible Gemini model.
    Returns (model_name_for_api, model_name_for_vision_parse) or None if not found.
    Both returned names are the full form (models/...) so vision-parse's client gets a valid ID.
    """
    accessible = _list_accessible_gemini_models(api_key)
    if not accessible:
        return None
    requested_norm = _normalize_gemini_model_name(requested)
    # Prefer exact match (with or without prefix)
    for full in accessible:
        if _normalize_gemini_model_name(full) == requested_norm:
            return (full, full)
    # Optional: prefer a short alias (e.g. gemini-2.0-flash -> models/gemini-2.0-flash)
    for full in accessible:
        if requested_norm in full or full.endswith("/" + requested_norm):
            return (full, full)
    return None


def _is_transient_vision_error(exc: Exception) -> bool:
    """Return True if the vision/LLM error is transient and worth retrying (500, 429, 503, timeout)."""
    msg = (str(exc) or "").lower()
    if any(x in msg for x in ("404", "401", "403", "model not found", "not supported", "invalid", "api key")):
        return False
    if any(
        x in msg
        for x in (
            "500",
            "internal error",
            "429",
            "rate",
            "503",
            "timeout",
            "resourceexhausted",
            "unavailable",
        )
    ):
        return True
    cause = getattr(exc, "__cause__", None)
    if cause is not None:
        return _is_transient_vision_error(cause)
    return False


def _inject_gemini_models_into_vision_parse(api_key: str) -> None:
    """Register all accessible Gemini models in vision_parse's SUPPORTED_MODELS."""
    import vision_parse.constants as vp_constants
    accessible = _list_accessible_gemini_models(api_key)
    for full_name in accessible:
        short = _normalize_gemini_model_name(full_name)
        vp_constants.SUPPORTED_MODELS[short] = "gemini"
        vp_constants.SUPPORTED_MODELS[full_name] = "gemini"


def _extract_local_pymupdf(pdf_path: Path) -> list[str] | None:
    """Extract text from each PDF page using PyMuPDF. Returns list of page texts or None on error."""
    try:
        import fitz
    except ImportError:
        return None
    try:
        doc = fitz.open(pdf_path)
    except Exception:
        return None
    try:
        pages = []
        for page in doc:
            text = page.get_text("text", sort=True)
            pages.append(text or "")
        return pages
    except Exception:
        return None
    finally:
        doc.close()


def _extract_local_pymupdf4llm(pdf_path: Path) -> str | None:
    """Extract full document as markdown using pymupdf4llm (tables, structure). Returns None if unavailable or on error."""
    try:
        import pymupdf4llm
    except ImportError:
        return None
    try:
        return pymupdf4llm.to_markdown(str(pdf_path))
    except Exception:
        return None


def _extract_local_ocr_pymupdf(
    pdf_path: Path,
    language: str = "eng",
    dpi: int = 300,
) -> list[str] | None:
    """Extract text via Tesseract OCR per page using PyMuPDF's get_textpage_ocr. Returns list of page texts or None if OCR unavailable."""
    try:
        import fitz
    except ImportError:
        return None
    tessdata = os.environ.get("TESSDATA_PREFIX") or None
    if tessdata and not Path(tessdata).is_dir():
        tessdata = None
    try:
        doc = fitz.open(pdf_path)
    except Exception:
        return None
    try:
        pages = []
        for page in doc:
            try:
                tp = page.get_textpage_ocr(
                    language=language,
                    dpi=dpi,
                    full=True,
                    tessdata=tessdata,
                )
                text = page.get_text("text", sort=True, textpage=tp)
                pages.append(text or "")
            except Exception:
                pages.append("")
        return pages
    except Exception:
        return None
    finally:
        doc.close()


def _strip_sa_exam_header(first_page_text: str) -> str:
    """Remove common SA Exam Papers boilerplate from the start of the first page."""
    marker = "www.saexampapers.co.za"
    idx = first_page_text.find(marker)
    if idx == -1:
        return first_page_text
    after = idx + len(marker)
    rest = first_page_text[after:].lstrip("\n\r\t ")
    return rest


def _build_markdown_from_pages(
    pdf_path: Path, pages: list[str], strip_header: bool = False
) -> str:
    """Build markdown string with Source header and --- Page N --- separators."""
    source_line = "Source: {}\n\n".format(pdf_path.resolve().as_uri())
    parts = [source_line]
    for i, content in enumerate(pages):
        if i > 0:
            parts.append("\n\n--- Page {} ---\n\n".format(i + 1))
        if strip_header and i == 0 and content:
            content = _strip_sa_exam_header(content)
        parts.append(content or "")
    return "".join(parts)


def _table_rows_to_markdown(rows: list[list[str | None]]) -> str:
    """Convert table rows (from pdfplumber table.extract()) to markdown table."""
    if not rows:
        return ""
    # Normalize cell strings
    def cell(c: str | None) -> str:
        return (c or "").strip().replace("\n", " ").replace("|", "\\|")

    normalized = [[cell(c) for c in row] for row in rows]
    col_count = max(len(r) for r in normalized) if normalized else 0
    if col_count == 0:
        return ""
    # Pad rows to same length
    for row in normalized:
        while len(row) < col_count:
            row.append("")
    header = normalized[0]
    sep = "| " + " | ".join("---" for _ in header) + " |"
    lines = ["| " + " | ".join(header) + " |", sep]
    for row in normalized[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


# Regex patterns for question/section headers (SA exam style)
_QUESTION_HEADER_RE = re.compile(
    r"^(?:(?:QUESTION|Vraag|VRAAG)\s+(\d+)|(\d+\.\d+)|(?:SOURCE\s+)([\w\d]+))\s*",
    re.IGNORECASE,
)


def _is_question_header(line_text: str) -> str | None:
    """If line_text looks like a question header, return question id (e.g. '1', '1.1', '1A'); else None."""
    line_text = (line_text or "").strip()
    if not line_text:
        return None
    m = _QUESTION_HEADER_RE.match(line_text)
    if m:
        g1, g2, g3 = m.group(1), m.group(2), m.group(3)
        if g1:
            return g1
        if g2:
            return g2
        if g3:
            return g3
    # Sub-question pattern at start of line: "1.1 ", "2.3 "
    if re.match(r"^\d+\.\d+\s", line_text):
        return re.match(r"^(\d+\.\d+)", line_text).group(1)
    return None


def _extract_by_question_pdfplumber(
    pdf_path: Path,
    output_path: Path | None,
    include_images: bool,
) -> str:
    """
    Extract PDF content by question regions using pdfplumber; return markdown with
    ## Question N sections. If include_images, render each question region to PNG
    in {output_stem}_assets/ and link in markdown.
    """
    import pdfplumber

    source_line = "Source: {}\n\n".format(pdf_path.resolve().as_uri())
    parts: list[str] = [source_line]

    with pdfplumber.open(pdf_path) as pdf:
        # Collect (question_id, page_number, top) for each header
        headers: list[tuple[str, int, float]] = []
        # Words per page: list of (top, bottom, x0, x1, text)
        words_by_page: dict[int, list[tuple[float, float, float, float, str]]] = {}

        for page in pdf.pages:
            pnum = page.page_number
            try:
                wlist = page.extract_words(keep_blank_chars=False) or []
            except Exception:
                wlist = []
            page_words: list[tuple[float, float, float, float, str]] = []
            for w in wlist:
                top = float(w.get("top", 0))
                bottom = float(w.get("bottom", top))
                x0 = float(w.get("x0", 0))
                x1 = float(w.get("x1", 0))
                text = (w.get("text") or "").strip()
                if text:
                    page_words.append((top, bottom, x0, x1, text))
            words_by_page[pnum] = page_words

            # Group into lines (same top within 3px)
            if not page_words:
                continue
            sorted_words = sorted(page_words, key=lambda x: (x[0], x[2]))
            line_top = sorted_words[0][0]
            line_texts: list[str] = []
            for top, bottom, x0, x1, text in sorted_words:
                if abs(top - line_top) <= 3:
                    line_texts.append(text)
                else:
                    line_str = " ".join(line_texts).strip()
                    qid = _is_question_header(line_str)
                    if qid:
                        headers.append((qid, pnum, line_top))
                    line_top = top
                    line_texts = [text]
            if line_texts:
                line_str = " ".join(line_texts).strip()
                qid = _is_question_header(line_str)
                if qid:
                    headers.append((qid, pnum, line_top))

        if not headers:
            # No questions detected: fall back to one section per page
            for page in pdf.pages:
                pnum = page.page_number
                text = (page.extract_text(layout=True) or "").strip()
                tables = page.find_tables()
                table_md: list[str] = []
                for t in tables:
                    rows = t.extract()
                    if rows:
                        table_md.append(_table_rows_to_markdown(rows))
                block = (text + "\n\n" + "\n\n".join(table_md)).strip()
                parts.append("\n## Page {}\n\n".format(pnum))
                parts.append(block or "")
                parts.append("\n")
            return "".join(parts).strip()

        # Sort headers by (page, top) to get question order
        headers.sort(key=lambda h: (h[1], h[2]))
        # Unique question ids in order
        seen: set[str] = set()
        ordered_ids: list[str] = []
        for qid, _, _ in headers:
            if qid not in seen:
                seen.add(qid)
                ordered_ids.append(qid)

        # Assign each word to the last header that is at or above it
        # (page, top) of header <= (page, top) of word
        question_bboxes: dict[str, dict[int, tuple[float, float, float, float]]] = {}
        for qid in ordered_ids:
            question_bboxes[qid] = {}

        for pnum, page_words in words_by_page.items():
            page_headers = [(q, p, t) for q, p, t in headers if p == pnum]
            page_headers.sort(key=lambda h: h[2])
            for top, bottom, x0, x1, text in page_words:
                # Find last header with top <= this word's top
                chosen_qid = None
                for qid, _, htop in page_headers:
                    if htop <= top + 2:
                        chosen_qid = qid
                if chosen_qid is None and page_headers:
                    chosen_qid = page_headers[0][0]
                if chosen_qid is not None:
                    if pnum not in question_bboxes[chosen_qid]:
                        question_bboxes[chosen_qid][pnum] = (x0, top, x1, bottom)
                    else:
                        ox0, otop, ox1, obottom = question_bboxes[chosen_qid][pnum]
                        question_bboxes[chosen_qid][pnum] = (
                            min(ox0, x0),
                            min(otop, top),
                            max(ox1, x1),
                            max(obottom, bottom),
                        )

        # Optional: assets dir for region images
        assets_dir: Path | None = None
        if include_images and output_path and str(output_path) != "-":
            stem = Path(output_path).stem
            assets_dir = Path(output_path).parent / "{}_assets".format(stem)
            assets_dir.mkdir(parents=True, exist_ok=True)

        for qid in ordered_ids:
            parts.append("\n## Question {}\n\n".format(qid))
            page_bboxes = question_bboxes.get(qid, {})
            if not page_bboxes:
                parts.append("")
                continue

            for pnum in sorted(page_bboxes.keys()):
                page = pdf.pages[pnum - 1]
                bbox = page_bboxes[pnum]
                x0, top, x1, bottom = bbox
                # Add small margin
                margin = 5
                crop_bbox = (
                    max(0, x0 - margin),
                    max(0, top - margin),
                    min(page.width, x1 + margin),
                    min(page.height, bottom + margin),
                )
                try:
                    cropped = page.crop(crop_bbox)
                except Exception:
                    cropped = page
                text = (cropped.extract_text(layout=True) or "").strip()
                tables = cropped.find_tables()
                table_md_list: list[str] = []
                for t in tables:
                    rows = t.extract()
                    if rows:
                        table_md_list.append(_table_rows_to_markdown(rows))
                if text:
                    parts.append(text)
                    parts.append("\n\n")
                if table_md_list:
                    parts.append("\n\n".join(table_md_list))
                    parts.append("\n\n")

                if assets_dir:
                    safe_id = re.sub(r"[^\w\-.]", "-", qid)
                    img_name = "question-{}-p{}.png".format(safe_id, pnum)
                    img_path = assets_dir / img_name
                    try:
                        import fitz
                        doc = fitz.open(pdf_path)
                        pag = doc[pnum - 1]
                        rect = fitz.Rect(crop_bbox[0], crop_bbox[1], crop_bbox[2], crop_bbox[3])
                        pix = pag.get_pixmap(clip=rect, alpha=False)
                        pix.save(str(img_path))
                        doc.close()
                    except Exception:
                        pass
                    else:
                        rel = "{}_assets/{}".format(Path(output_path).stem, img_name)
                        parts.append("\n![Question {}]({})\n\n".format(qid, rel))

    return "".join(parts).strip()


def convert(
    pdf_path: str | Path,
    output_path: str | Path | None,
    model_override: str | None,
    local_only: bool = False,
    vision_only: bool = False,
    strip_header: bool = False,
    use_rich: bool = False,
    by_question: bool = False,
    no_images: bool = False,
    by_question_images: bool = False,
    use_ocr: bool = False,
    ocr_language: str = "eng",
    ocr_dpi: int = 300,
) -> None:
    """Convert PDF to markdown and write to output_path or stdout. Tries local (PyMuPDF) first unless --vision."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists() or not pdf_path.is_file():
        print("Error: PDF file not found:", pdf_path, file=sys.stderr)
        sys.exit(1)
    if pdf_path.suffix.lower() != ".pdf":
        print("Error: File is not a PDF:", pdf_path, file=sys.stderr)
        sys.exit(1)

    def write_output(markdown: str) -> None:
        if output_path is None or str(output_path) == "-":
            print(markdown, end="")
            return
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(markdown, encoding="utf-8")

    if by_question:
        try:
            import pdfplumber  # noqa: F401
        except ImportError:
            print(
                "Error: --by-question requires pdfplumber. Install with: pip install pdfplumber",
                file=sys.stderr,
            )
            sys.exit(1)
        out_path = Path(output_path) if output_path and str(output_path) != "-" else None
        # Region images off by default to avoid saving PNGs of text; use --images to enable (e.g. for diagrams).
        markdown = _extract_by_question_pdfplumber(
            pdf_path, out_path, include_images=by_question_images
        )
        write_output(markdown)
        return

    if not vision_only and use_rich:
        rich_md = _extract_local_pymupdf4llm(pdf_path)
        if rich_md is not None and rich_md.strip():
            source_line = "Source: {}\n\n".format(pdf_path.resolve().as_uri())
            write_output(source_line + rich_md.strip() + "\n")
            return

    if not vision_only and use_ocr:
        ocr_pages = _extract_local_ocr_pymupdf(
            pdf_path, language=ocr_language, dpi=ocr_dpi
        )
        if ocr_pages is not None and any(p.strip() for p in ocr_pages):
            markdown = _build_markdown_from_pages(
                pdf_path, ocr_pages, strip_header=strip_header
            )
            write_output(markdown)
            return
        if local_only:
            print(
                "Error: OCR failed or produced no text; is Tesseract installed and TESSDATA_PREFIX set?",
                file=sys.stderr,
            )
            sys.exit(1)
        # OCR failed and not local_only: fall through to vision-parse

    if not vision_only and not use_ocr:
        local_pages = _extract_local_pymupdf(pdf_path)
        if local_pages is not None and any(p.strip() for p in local_pages):
            markdown = _build_markdown_from_pages(
                pdf_path, local_pages, strip_header=strip_header
            )
            write_output(markdown)
            return
        empty_threshold = 50
        total_chars = sum(len(p or "") for p in (local_pages or []))
        if (local_pages is not None and total_chars < empty_threshold) or local_pages is None:
            ocr_pages = _extract_local_ocr_pymupdf(
                pdf_path, language=ocr_language, dpi=ocr_dpi
            )
            if ocr_pages is not None and any(p.strip() for p in ocr_pages):
                markdown = _build_markdown_from_pages(
                    pdf_path, ocr_pages, strip_header=strip_header
                )
                write_output(markdown)
                return
        if local_only:
            print(
                "Error: Local extraction produced no text; try without --local to use vision-parse.",
                file=sys.stderr,
            )
            sys.exit(1)

    from vision_parse import VisionParser
    from vision_parse.llm import LLMError
    from vision_parse.parser import VisionParserError, UnsupportedFileError

    config = _get_config()
    if model_override is not None:
        config["model_name"] = model_override
    api_key = _get_api_key(config)
    if not _is_ollama_model(config["model_name"]) and not api_key:
        print(
            "Error: API key required for model '{}'. Set OPENAI_API_KEY or GOOGLE_API_KEY (or GEMINI_API_KEY).".format(
                config["model_name"]
            ),
            file=sys.stderr,
        )
        sys.exit(1)

    model_name = config["model_name"]
    if "gemini" in (model_name or "").lower() and api_key:
        _inject_gemini_models_into_vision_parse(api_key)
        resolved = _resolve_gemini_model(model_name, api_key)
        if resolved is None:
            accessible = _list_accessible_gemini_models(api_key)
            examples = sorted(_normalize_gemini_model_name(n) for n in accessible)[:5]
            print(
                "Error: Gemini model '{}' is not available for your API key. Example models you can use: {}.".format(
                    model_name, ", ".join(examples)
                ),
                file=sys.stderr,
            )
            sys.exit(1)
        model_name = resolved[0]

    try:
        max_retries = int(os.environ.get("PDF2MD_VISION_MAX_RETRIES", "3"))
    except (TypeError, ValueError):
        max_retries = 3
    max_retries = max(0, max_retries)
    try:
        base_delay_sec = float(os.environ.get("PDF2MD_VISION_RETRY_BACKOFF_SEC", "5"))
    except (TypeError, ValueError):
        base_delay_sec = 5.0
    backoff_factor = 3.0

    pages = None
    last_error: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            parser = VisionParser(
                model_name=model_name,
                api_key=api_key,
                temperature=config["temperature"],
                top_p=config["top_p"],
                image_mode=config["image_mode"],
                detailed_extraction=False,
                enable_concurrency=False,
            )
            pages = parser.convert_pdf(pdf_path)
            last_error = None
            break
        except LLMError as e:
            last_error = e
            if _is_transient_vision_error(e) and attempt < max_retries:
                delay = base_delay_sec * (backoff_factor ** attempt)
                print(
                    "Vision API error ({}). Retrying in {:.0f}s (attempt {}/{})...".format(
                        str(e).strip()[:80], delay, attempt + 1, max_retries
                    ),
                    file=sys.stderr,
                )
                time.sleep(delay)
            else:
                break
        except (VisionParserError, UnsupportedFileError, FileNotFoundError) as e:
            print("Error:", e, file=sys.stderr)
            sys.exit(1)

    if pages is None and last_error is not None:
        print("Error:", last_error, file=sys.stderr)
        sys.exit(1)

    markdown = _build_markdown_from_pages(
        pdf_path, pages, strip_header=strip_header
    )
    write_output(markdown)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a PDF to markdown. Tries local (PyMuPDF) first, then vision-parse. Output includes a Source: header."
    )
    parser.add_argument(
        "pdf_path",
        type=Path,
        help="Path to a PDF file or a directory containing PDFs (converts all .pdf files in the directory).",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Output path for markdown file. Default: <pdf_stem>.md next to the PDF. Use '-' for stdout. Ignored when input is a directory.",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default=None,
        help="Model name (overrides PDF2MD_MODEL). e.g. llama3.2-vision:11b, gpt-4o, gemini-2.5-flash",
    )
    parser.add_argument(
        "--local",
        action="store_true",
        help="Use only local extraction (PyMuPDF); do not call vision-parse. Fail if no text extracted.",
    )
    parser.add_argument(
        "--vision",
        action="store_true",
        help="Skip local extraction and use only vision-parse (Vision LLM).",
    )
    parser.add_argument(
        "--strip-header",
        action="store_true",
        help="Remove common SA Exam Papers boilerplate from the first page (text up to www.saexampapers.co.za).",
    )
    parser.add_argument(
        "--rich",
        action="store_true",
        help="Use pymupdf4llm for local extraction (markdown tables, structure). Single file only. Requires: pip install pymupdf4llm.",
    )
    parser.add_argument(
        "--by-question",
        action="store_true",
        help="Extract by question regions (pdfplumber): segment by question headers, crop, output ## Question N sections. Single file only.",
    )
    parser.add_argument(
        "--images",
        action="store_true",
        help="With --by-question: write per-question region PNGs to *_assets/ (e.g. for diagrams). Off by default to avoid saving images of text.",
    )
    parser.add_argument(
        "--no-images",
        action="store_true",
        help="With --by-question: same as default (no region PNGs). Kept for backwards compatibility.",
    )
    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Use local OCR (Tesseract) only; skip normal text extraction. Requires Tesseract and TESSDATA_PREFIX.",
    )
    parser.add_argument(
        "--ocr-language",
        type=str,
        default=os.environ.get("PDF2MD_OCR_LANG", "eng"),
        help="Tesseract language(s), e.g. eng or eng+afr (default: PDF2MD_OCR_LANG or eng).",
    )
    parser.add_argument(
        "--ocr-dpi",
        type=int,
        default=300,
        help="DPI for OCR render (default: 300).",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    if pdf_path.is_dir():
        if args.by_question:
            print(
                "Error: --by-question is single-file only; pass a PDF file, not a directory.",
                file=sys.stderr,
            )
            sys.exit(1)
        pdfs = sorted(pdf_path.glob("*.pdf"))
        if not pdfs:
            print("Error: No PDF files found in directory:", pdf_path, file=sys.stderr)
            sys.exit(1)
        failed = 0
        for i, one_pdf in enumerate(pdfs):
            out = one_pdf.with_suffix(".md")
            print("[{}/{}] {}".format(i + 1, len(pdfs), one_pdf.name), file=sys.stderr)
            try:
                convert(
                    one_pdf,
                    out,
                    args.model,
                    local_only=args.local,
                    vision_only=args.vision,
                    strip_header=args.strip_header,
                    use_rich=args.rich,
                    by_question=args.by_question,
                    no_images=args.no_images,
                    by_question_images=args.images,
                    use_ocr=args.ocr,
                    ocr_language=args.ocr_language,
                    ocr_dpi=args.ocr_dpi,
                )
            except SystemExit as e:
                if e.code != 0:
                    failed += 1
                    print("Failed:", one_pdf.name, file=sys.stderr)
        if failed:
            sys.exit(1)
        return

    output_path: str | Path | None = args.output
    if output_path is None:
        output_path = args.pdf_path.with_suffix(".md")

    convert(
        args.pdf_path,
        output_path,
        args.model,
        local_only=args.local,
        vision_only=args.vision,
        strip_header=args.strip_header,
        use_rich=args.rich,
        by_question=args.by_question,
        no_images=args.no_images,
        by_question_images=args.images,
        use_ocr=args.ocr,
        ocr_language=args.ocr_language,
        ocr_dpi=args.ocr_dpi,
    )


if __name__ == "__main__":
    main()
