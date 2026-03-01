# Review: pdf2markdown extraction output (Exams – 19 files)

**Run:** `--local --strip-header` on `Pdfs for test/Exams`  
**Date:** 2025

---

## 1. Format and structure

| Check | Status |
|-------|--------|
| `Source: file:///...` header on every file | Pass |
| `--- Page N ---` separators | Pass (all 19 files) |
| SA Exam Papers boilerplate stripped from first page where present | Pass (history memo, etc. start at SENIOR CERTIFICATE or content) |
| UTF-8; no replacement characters in sampled text-based files | Pass |

---

## 2. Content quality by type

**Strong extraction (text-based PDFs)**  
- **History memo (Eng/Afr), English FAL P1, Sesotho SAL memo, Siswati FAL P1, Xitsonga memos/QPs, Setswana, South African Sign Language memo:** First page correctly stripped where applicable; body text, headings, bullets, and language-specific characters (Sesotho, Siswati, Setswana, Xitsonga, Afrikaans) are intact and readable. Page counts and structure match expectations.

**Partial / problematic**

- **Life-Orientation-Grade-12-NSC-QP-October-2024-Supplementary.pdf**  
  - **Issue:** Almost only the watermark appears: “SA EXAM PAPERS | This past paper was downloaded from saexampapers.co.za” on every page.  
  - **Cause:** Likely image-based (scanned) PDF with little or no selectable text; PyMuPDF only sees the watermark.  
  - **Recommendation:** Run with `--vision` (vision-parse) for this file so the Vision LLM can read the page images.

- **Life-Orientation-Grade-12-NSC-QP-September-2025-Afr-Eastern-Cape.pdf**  
  - **Issue:** After the watermark, many lines are garbled (e.g. `?9<: ?7`, `9  <:;%9 ; <D<A??`, `>;??$%!&`, `7 8  9:;<=  ;<>`). Some readable fragments remain.  
  - **Cause:** Probable custom fonts or encoding that PyMuPDF’s text extraction does not map correctly to Unicode.  
  - **Recommendation:** Try `--vision` for this PDF as well; optionally try `--rich` (pymupdf4llm) to see if layout/structure helps.

---

## 3. Strip-header behaviour

- Files that had the “You have Downloaded… www.saexampapers.co.za” block on page 1 now start with blank lines and then `--- Page 2 ---` (or real content on page 1 when the block was absent). No over-stripping observed.
- PDFs whose first page does not contain “www.saexampapers.co.za” (e.g. “Confidential” only) are unchanged on page 1; no false positives.

---

## 4. Page counts (sample)

| File | Page separators | Note |
|------|-----------------|------|
| history_p1_2019_may-june_MEMO (Eng) | 24 | 25 pages |
| ee3aade3b70f-sesotho-puo-ya-tlatsetso...mg | 7 | 8 pages |
| English FAL P1 May-June 2025 | 13 | 14 pages |
| Life-Orientation Oct 2024 Supplementary | 9 | 10 pages (watermark only) |
| fb6ccd96375a-south-african-sign-language...mg | 27 | 28 pages |
| e522737a864e-siswati-lulwimi-lwasekhaya-hl-p2...qp | 26 | 27 pages |

Page boundaries are consistent across the set.

---

## 5. Summary and recommendations

- **17 of 19** files have good, usable markdown for RAG/search or pipeline ingestion. Structure and languages (EN, AF, Sesotho, Siswati, Setswana, Xitsonga, SASL) are preserved; strip-header behaves as intended.
- **2 Life Orientation PDFs** need special handling:
  - **Oct 2024 Supplementary:** Use `--vision` (vision-parse) to extract content from the page images.
  - **Sept 2025 Eastern Cape (Afr):** Use `--vision` (and optionally try `--rich`) to avoid encoding/garbling from the current text layer.

**Suggested commands for the two Life Orientation files:**

```bash
python pdf2markdown/convert.py "Pdfs for test/Exams/Life-Orientation-Grade-12-NSC-QP-October-2024-Supplementary.pdf" --vision --strip-header -o "Pdfs for test/Exams/Life-Orientation-Grade-12-NSC-QP-October-2024-Supplementary.md"

python pdf2markdown/convert.py "Pdfs for test/Exams/Life-Orientation-Grade-12-NSC-QP-September-2025-Afr-Eastern-Cape.pdf" --vision --strip-header -o "Pdfs for test/Exams/Life-Orientation-Grade-12-NSC-QP-September-2025-Afr-Eastern-Cape.md"
```

(Requires Gemini/API key configured for vision-parse.)
