FROM python:3.11-slim

# Install Tesseract OCR engine + English language data
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pdf2markdown

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the converter script
COPY convert.py .

# API keys and model config are passed at runtime via -e flags (not baked in)
# TESSDATA_PREFIX is auto-detected by Tesseract when installed via apt

ENTRYPOINT ["python", "convert.py"]
