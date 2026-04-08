# MAIL AI AGENT

AI-powered email assistant to extract, enrich, score, and draft B2B outreach emails using OpenRouter.

## Project Structure

This project uses a Modular Monolith architecture:
- `backend/`: Python + FastAPI API server and SQLite task queue.
- `frontend/`: React + Electron UI.

## Getting Started

### 1. Backend Setup
1. Navigate to `backend/`:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables (e.g. `DATABASE_URL`, `OPENROUTER_API_KEY`, etc. in a `.env` file).
4. Run migrations and seed the database:
   ```bash
   alembic upgrade head
   python src/core/seeder.py
   ```
5. Start the API server:
   ```bash
   uvicorn src.main:app --reload
   ```
6. (In a separate terminal) Start the background worker:
   ```bash
   huey_consumer src.core.queue.huey
   ```

### 2. Frontend Setup
1. Navigate to `frontend/`:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the application (starts Vite dev server and Electron):
   ```bash
   npm run electron:dev
   ```
