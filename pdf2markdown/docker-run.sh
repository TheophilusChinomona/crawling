#!/usr/bin/env bash
# pdf2markdown/docker-run.sh
# Run convert.py inside Docker with Tesseract OCR + Gemini fallback.
#
# Usage:
#   ./pdf2markdown/docker-run.sh <pdf-file-or-folder> [convert.py args...]
#
# Examples:
#   ./pdf2markdown/docker-run.sh "Pdfs for test/my folder" --ocr
#   ./pdf2markdown/docker-run.sh "Pdfs for test/doc.pdf" --ocr -o /data/out.md
#
# Environment variables (read from shell or .env next to this script):
#   GEMINI_API_KEY   — required for Gemini vision fallback
#   PDF2MD_MODEL     — optional, default: gemini-2.0-flash-exp
#   PDF2MD_OCR_LANG  — optional Tesseract language(s), default: eng
#
# Flags:
#   --build   Force rebuild the Docker image before running

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE_NAME="pdf2markdown"

# Load .env from the script directory if variables are not already set
if [ -f "$SCRIPT_DIR/.env" ]; then
    set -o allexport
    # shellcheck disable=SC1091
    source "$SCRIPT_DIR/.env"
    set +o allexport
fi

# Parse --build flag
FORCE_BUILD=0
ARGS=()
for arg in "$@"; do
    if [ "$arg" = "--build" ]; then
        FORCE_BUILD=1
    else
        ARGS+=("$arg")
    fi
done
set -- "${ARGS[@]+"${ARGS[@]}"}"

INPUT="${1:?Usage: $0 <pdf-file-or-folder> [convert.py args...]}"
shift

# Build image if it doesn't exist or --build was passed
if [ "$FORCE_BUILD" = "1" ] || ! docker image inspect "$IMAGE_NAME" &>/dev/null; then
    echo "[pdf2md] Building Docker image..." >&2
    docker build -t "$IMAGE_NAME" "$SCRIPT_DIR"
fi

# Resolve input to an absolute path
INPUT_ABS="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"

# Mount the directory containing the input; adjust container path accordingly
if [ -d "$INPUT_ABS" ]; then
    MOUNT_DIR="$INPUT_ABS"
    CONTAINER_INPUT="/data"
else
    MOUNT_DIR="$(dirname "$INPUT_ABS")"
    CONTAINER_INPUT="/data/$(basename "$INPUT_ABS")"
fi

# MSYS_NO_PATHCONV=1 prevents Git Bash on Windows from mangling /data into a Windows path
MSYS_NO_PATHCONV=1 docker run --rm \
    -v "$MOUNT_DIR:/data" \
    -e GEMINI_API_KEY="${GEMINI_API_KEY:-}" \
    -e PDF2MD_MODEL="${PDF2MD_MODEL:-gemini-2.0-flash-exp}" \
    -e PDF2MD_OCR_LANG="${PDF2MD_OCR_LANG:-eng}" \
    "$IMAGE_NAME" \
    "$CONTAINER_INPUT" "$@"
