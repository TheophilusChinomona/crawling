# Audit: pdf2markdown extraction output (Exams folder)

**Date:** 2025  
**Source:** `Pdfs for test/Exams` (5 PDFs)  
**Method:** Local extraction (PyMuPDF), no vision-parse.

---

## 1. Format compliance

| Check | Status |
|-------|--------|
| `Source: file:///...` header on every file | Pass |
| `--- Page N ---` separators between pages | Pass |
| UTF-8 text, no replacement characters (U+FFFD) in sampled content | Pass |
| One markdown file per PDF, same base name (`.md` next to `.pdf`) | Pass |

---

## 2. Page counts

| File | Separators ("--- Page N ---") | Implied pages | Notes |
|------|-------------------------------|---------------|--------|
| history_p1_2019_may-june_MEMO_History-P1-May-June-2019-Memo-Eng.md | 24 | 25 | Doc states "24 pages" for guidelines (cover + 24) |
| history_p1_2019_november_MEMO_History-P1-May-June-2019-Memo-Afr.md | 24 | 25 | Same structure (Afrikaans memo) |
| history_p1_2019_may-june_QP_History-P1-May-June-2019-Addendum-Eng.md | 14 | 15 | Doc states "14 pages" for addendum |
| 0c831a99cd2b-xitsonga-ririmi-ra-le-kaya-hl-gr12-may-june-2025-mg.md | 8 | 9 | Doc states "9 tipheji" (9 pages) |
| history_p1_2019_november_QP_History-P1-Nov-2019-Eng.md | 9 | 10 | Doc states "9 pages" for question paper |

Page structure is consistent with stated document lengths.

---

## 3. Content quality

- **English memos/addendum:** Text is readable; headings, bullet lists, and paragraphs are preserved. Numbering (1.1, 1.2, SOURCE 1A, etc.) is intact.
- **Afrikaans memo:** Same structure; Afrikaans characters (e.g. “Nasienriglyne”, “Geskiedenis”) render correctly.
- **Xitsonga memo:** Xitsonga text (e.g. “XILETELO XA MAKOREKETELO”, “tirhiwa”) is present and readable.
- **Tables:** PyMuPDF `get_text("text", sort=True)` flattens tables into lines. Multi-column layouts (e.g. cognitive levels / weighting tables) appear as run-on or wrapped lines rather than markdown tables. Acceptable for plain-text extraction; for structured tables, consider `pymupdf4llm` or vision-parse later.
- **Boilerplate:** First page of several PDFs (“SA Exam Papers”, “www.saexampapers.co.za”) is extracted as-is; can be stripped downstream if not needed.
- **Symbols:** Isolated symbols (e.g. check/tick) may appear as a different character or space in the raw text; no systematic replacement-character (�) issues in the sampled files.

---

## 4. Line counts (rough size check)

| Markdown file | Lines |
|---------------|-------|
| history_p1_2019_may-june_MEMO_History-P1-May-June-2019-Memo-Eng.md | 1 215 |
| history_p1_2019_november_MEMO_History-P1-May-June-2019-Memo-Afr.md | 1 211 |
| history_p1_2019_may-june_QP_History-P1-May-June-2019-Addendum-Eng.md | 563 |
| 0c831a99cd2b-xitsonga-ririmi-ra-le-kaya-hl-gr12-may-june-2025-mg.md | 406 |
| history_p1_2019_november_QP_History-P1-Nov-2019-Eng.md | 423 |

---

## 5. Issues and recommendations

1. **Tables:** Current pipeline does not emit markdown tables; table regions are linearized. For RAG/search this is often sufficient; for strict table reuse, consider adding `pymupdf4llm` or vision-parse for those PDFs.
2. **Cover/boilerplate:** First-page “SA Exam Papers” text is included in every affected file. Optional: add a post-step or option to strip a common header pattern.
3. **Ordering:** `sort=True` in `get_text()` improves reading order; complex multi-column or side-by-side layouts may still have ordering quirks on a few pages.
4. **No missing files:** All 5 PDFs produced a corresponding `.md`; no empty or failed outputs.

---

## 6. Verdict

Extraction is **fit for purpose** for downstream use (RAG, search, or ingestion into the LeadCrawl pipeline). Format is consistent, page boundaries are preserved, and multi-language content (EN, AF, Xitsonga) is intact. Tables are plain text only; if needed, enhance later with a table-aware or vision-based step.

---

## 7. Fixes applied (post-audit)

| Issue | Fix | How to use |
|-------|-----|------------|
| **Tables** flattened to plain text | Optional **rich** extraction via **pymupdf4llm** | `pip install pymupdf4llm` then run with `--rich`. Produces markdown tables and structure; single or batch. |
| **Boilerplate** (SA Exam Papers header) on first page | **Strip-header** option | Run with `--strip-header` to remove text from the start of the first page up to and including `www.saexampapers.co.za`. |
| **Ordering** in complex layouts | Use `--rich` (pymupdf4llm) or `--vision` | For difficult multi-column pages, `--rich` or `--vision` can give better reading order. |
