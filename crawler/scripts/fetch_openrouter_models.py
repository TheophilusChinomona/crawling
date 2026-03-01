"""
Fetch OpenRouter models and their capabilities from the API and write a structured YAML index.

The OpenRouter GET /api/v1/models endpoint returns all models with id, name, context_length,
architecture (modality, input/output modalities), supported_parameters, pricing, etc.
No API key is required for listing (key optional for auth).

Usage:
  python fetch_openrouter_models.py [--output PATH] [--api-key KEY]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import urllib.request
    import urllib.error
except ImportError:
    urllib = None  # type: ignore

MODELS_URL = "https://openrouter.ai/api/v1/models"


def _fetch_models(api_key: str | None) -> list[dict]:
    """GET OpenRouter models API; return list of model objects."""
    req = urllib.request.Request(MODELS_URL)
    if api_key:
        req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Accept", "application/json")
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode())
    return data.get("data") or []


def _price_is_zero(v: str | int | float | None) -> bool:
    """True if price is zero (free)."""
    if v is None:
        return True
    if isinstance(v, (int, float)):
        return v == 0
    try:
        return float(v) == 0
    except (TypeError, ValueError):
        return False


def _is_free_model(summary: dict) -> bool:
    """True if model has no charge for prompt and completion (free tier)."""
    pricing = summary.get("pricing") or {}
    prompt = pricing.get("prompt")
    completion = pricing.get("completion")
    return _price_is_zero(prompt) and _price_is_zero(completion)


def _model_summary(m: dict) -> dict:
    """Extract a stable subset of fields for the YAML index."""
    arch = m.get("architecture") or {}
    pricing = m.get("pricing") or {}
    return {
        "id": m.get("id"),
        "name": m.get("name"),
        "description": (m.get("description") or "").strip() or None,
        "context_length": m.get("context_length"),
        "modality": arch.get("modality"),
        "input_modalities": arch.get("input_modalities") or [],
        "output_modalities": arch.get("output_modalities") or [],
        "supported_parameters": m.get("supported_parameters") or [],
        "pricing": {k: v for k, v in pricing.items() if v is not None} or None,
        "top_provider": {
            "context_length": (m.get("top_provider") or {}).get("context_length"),
            "max_completion_tokens": (m.get("top_provider") or {}).get("max_completion_tokens"),
        }
        if m.get("top_provider")
        else None,
    }


def _write_model_block(f: object, s: dict) -> None:
    """Write a single model entry to the YAML file."""
    f.write(f"  - id: {json.dumps(s['id'])}\n")
    f.write(f"    name: {json.dumps(s.get('name') or '')}\n")
    if s.get("description"):
        f.write(f"    description: {json.dumps(s['description'][:200])}\n")
    if s.get("context_length") is not None:
        f.write(f"    context_length: {s['context_length']}\n")
    if s.get("modality"):
        f.write(f"    modality: {json.dumps(s['modality'])}\n")
    if s.get("input_modalities"):
        f.write(f"    input_modalities: {json.dumps(s['input_modalities'])}\n")
    if s.get("output_modalities"):
        f.write(f"    output_modalities: {json.dumps(s['output_modalities'])}\n")
    if s.get("supported_parameters"):
        f.write(f"    supported_parameters: {json.dumps(s['supported_parameters'])}\n")
    if s.get("pricing"):
        f.write(f"    pricing: {json.dumps(s['pricing'])}\n")
    f.write("\n")


def fetch_and_write_models_yaml(output_path: Path, api_key: str | None = None) -> int:
    """Fetch models from OpenRouter API and write models.yaml (and models.json) split by free vs paid."""
    models = _fetch_models(api_key)
    if not models:
        return 0
    summaries = [_model_summary(m) for m in models]
    free = [s for s in summaries if _is_free_model(s)]
    paid = [s for s in summaries if not _is_free_model(s)]
    out = {
        "source": MODELS_URL,
        "description": "OpenRouter models and capabilities (from API). Split by free (prompt+completion both 0) vs paid.",
        "count": len(summaries),
        "count_free": len(free),
        "count_paid": len(paid),
        "models": summaries,
        "free_models": free,
        "paid_models": paid,
    }
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    base = output_path.parent / output_path.stem
    # Write JSON (machine-readable)
    with open(base.with_suffix(".json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    # Write YAML with free and paid sections
    with open(base.with_suffix(".yaml"), "w", encoding="utf-8") as f:
        f.write("# OpenRouter models and capabilities (from API)\n")
        f.write(f"# Source: {MODELS_URL}\n")
        f.write("# Free = prompt and completion pricing both 0\n\n")
        f.write(f"count: {len(summaries)}\n")
        f.write(f"count_free: {len(free)}\n")
        f.write(f"count_paid: {len(paid)}\n\n")
        f.write("free_models:\n")
        for s in free:
            _write_model_block(f, s)
        f.write("paid_models:\n")
        for s in paid:
            _write_model_block(f, s)
    return len(summaries)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch OpenRouter models and capabilities and write models.yaml."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output path for models.yaml/.json (default: docs-crawl/openrouter-docs/models.yaml under repo root)",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("OPENROUTER_API_KEY"),
        help="OpenRouter API key (optional for listing models). Default: OPENROUTER_API_KEY env.",
    )
    args = parser.parse_args()
    if args.output is None:
        # Default: repo root is parent of crawler/
        repo_root = Path(__file__).resolve().parent.parent.parent
        args.output = repo_root / "docs-crawl" / "openrouter-docs" / "models.yaml"
    try:
        n = fetch_and_write_models_yaml(args.output, args.api_key)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    if n == 0:
        print("No models returned from API.", file=sys.stderr)
        return 1
    print(f"Wrote {n} models to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
