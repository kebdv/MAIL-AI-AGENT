# Quickstart

This document provides a high-level overview of the architectural decisions from Phase 1.

## Architecture: Modular Monolith
The application is built as a Modular Monolith.
- **Backend:** Python + FastAPI
- **Frontend:** React + Electron
- **Database:** local SQLite (via SQLAlchemy/SQLModel)
- **Async Processing:** Huey with `SqliteHuey` (or FastAPI BackgroundTasks). This avoids requiring the user to install heavy infrastructure like Redis locally.

## Core Pipeline
1. **Ingestion**: Upload a business card or PDF. The file is sent to OpenRouter Vision models to extract entities (Zero-shot extraction).
2. **Enrichment & Scoring**: The Lead is saved in SQLite and scored based on pre-defined criteria.
3. **Generation**: Qualified leads trigger generation of Bilingual drafts using OpenRouter Text models and stored Prompt templates.
4. **Delivery & Tracking**: Approved drafts are sent via standard SMTP, with interactions logged to the database.

## Development Workflow Setup (Future)
Once implementation begins, developers will run:
1. `uvicorn main:app --reload` for the FastAPI backend.
2. `huey_consumer.py main.huey` for background tasks.
3. `npm start` for the Electron application wrapper.
