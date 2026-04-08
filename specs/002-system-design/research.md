# Phase 0: Research & Technical Decisions

## 1. Queue Implementation for Local Python + Electron App
- **Decision**: Huey with `SqliteHuey` (or FastAPI `BackgroundTasks` + SQLite if lightweight)
- **Rationale**: The application needs asynchronous processing for OCR and LLM calls, but requiring local infrastructure like Redis or RabbitMQ is a terrible user experience for a packaged desktop application. Huey provides real queue capabilities (retries, dead-letter queues) using just a local SQLite file, which aligns perfectly with our SQLite storage choice.
- **Alternatives considered**: Celery/RQ/Dramatiq (rejected: require Redis/RabbitMQ which are hard to bundle), FastAPI BackgroundTasks (acceptable but lacks advanced retry/queue features out of the box).

## 2. OCR Tooling for Business Cards and PDFs
- **Decision**: Vision Models (e.g. GPT-4o or Claude 3.5 Sonnet) accessed exclusively via OpenRouter.
- **Rationale**: The Constitution mandates (Principle III & V) that extraction from business cards and PDFs MUST be done using Vision models via OpenRouter. This bypasses the need for dedicated OCR pipelines (like Azure AI or Tesseract) and allows for Zero-shot entity extraction directly into structured JSON. It perfectly handles the bi-directional text and complex layouts of Arabic/English business cards natively.
- **Alternatives considered**: Azure AI Document Intelligence (rejected: violates OpenRouter-only mandate), Tesseract (rejected: poor accuracy without massive engineering overhead for bi-directional text and layout parsing).

## 3. Bilingual Prompt Engineering
- **Decision**: System prompts written in English utilizing XML tags for structure, with explicit rules for "Transcreation" to MENA business culture and a strict glossary.
- **Rationale**: Top-tier models (GPT-4/Claude 3 via OpenRouter) process logic best in English. Instructing the model in English to output Modern Standard Arabic (MSA) using XML tags (`<localization-rules>`) ensures high compliance. Furthermore, explicitly commanding "Transcreation" over "Translation" ensures the output respects Arabic business etiquette (e.g., using proper titles instead of direct translated casual English greetings like "Hi").
- **Alternatives considered**: Writing prompts entirely in Arabic (rejected: degrades the model's ability to follow complex multi-step instructions), Transliteration of technical terms (rejected: looks unprofessional; a glossary is preferred).
