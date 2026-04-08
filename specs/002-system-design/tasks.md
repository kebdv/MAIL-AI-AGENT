# Tasks: System Design Documentation and Architecture Setup

**Input**: Design documents from `/specs/002-system-design/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Initialize backend Python project with FastAPI, SQLAlchemy, and Huey dependencies in `backend/`
- [X] T002 Initialize frontend project with React, Vite, and Electron in `frontend/`
- [X] T003 [P] Configure linting (Ruff for backend, ESLint for frontend)
- [X] T004 [P] Configure testing frameworks (pytest for backend, vitest for frontend)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**🚨 CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Setup database connection and session management in `backend/src/core/database.py` (SQLite)
- [X] T006 [P] Setup background task queue infrastructure in `backend/src/core/queue.py` (SqliteHuey)
- [X] T007 Configure backend environment variables and settings management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - System Architecture & Component Mapping (Priority: P1) 🏆 MVP

**Goal**: Establish the high-level components (Ingestion, Enrichment, AI Generation, Delivery, Tracking) and their boundaries.

**Independent Test**: The backend can be launched and exposes the base API structure for all core modules, and the Electron app successfully starts and connects.

### Implementation for User Story 1

- [X] T008 [US1] Create component directory structure for `backend/src/modules/` (ingestion, enrichment, generation, delivery)
- [X] T009 [P] [US1] Implement FastAPI application entrypoint in `backend/src/main.py`
- [X] T010 [P] [US1] Implement Electron main process entrypoint in `frontend/main.js`
- [X] T011 [P] [US1] Create placeholder React frontend interface in `frontend/src/App.tsx`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Database Schema & Data Modeling (Priority: P2)

**Goal**: Implement the persistence layer for Leads, Companies, and Interactions as defined in the data model.

**Independent Test**: Database tables can be created via migrations and match the Data Model spec.

### Implementation for User Story 2

- [X] T012 [P] [US2] Create Company and Lead SQLAlchemy models in `backend/src/core/models/lead.py`
- [X] T013 [P] [US2] Create OutreachDraft SQLAlchemy model in `backend/src/core/models/draft.py`
- [X] T014 [P] [US2] Create InteractionLog SQLAlchemy model in `backend/src/core/models/interaction.py`
- [X] T015 [P] [US2] Create SystemPrompt SQLAlchemy model in `backend/src/core/models/prompt.py`
- [X] T016 [US2] Setup Alembic and generate initial migration for the SQLite database
- [X] T017 [US2] Create database seeder script to populate default English/Arabic system prompts

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - API Contracts & External Integrations (Priority: P3)

**Goal**: Implement clear API contracts and integration specifications for the backend modules.

**Independent Test**: FastAPI docs (Swagger UI) show all expected endpoints, and automated tests pass for router inputs/outputs.

### Tests for User Story 3

- [X] T018 [P] [US3] Write contract tests for core API endpoints in `backend/tests/test_api_contracts.py`

### Implementation for User Story 3

- [X] T019 [P] [US3] Implement Ingestion API router in `backend/src/modules/ingestion/router.py` based on POST /api/v1/ingest/document
- [X] T020 [P] [US3] Implement Enrichment API router in `backend/src/modules/enrichment/router.py` based on POST /api/v1/enrich
- [X] T021 [P] [US3] Implement Generation API router in `backend/src/modules/generation/router.py` based on POST /api/v1/generate-draft
- [X] T022 [P] [US3] Implement Delivery API router in `backend/src/modules/delivery/router.py` based on POST /api/v1/delivery/send
- [X] T023 [US3] Setup OpenRouter API client abstraction in `backend/src/core/ai.py`
- [X] T024 [US3] Setup SMTP client abstraction in `backend/src/core/delivery.py`
- [X] T025 [US3] Register all module routers in `backend/src/main.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T026 [P] Configure Dead Letter Queue structure for Huey in `backend/src/core/queue.py`
- [X] T027 [P] Update `README.md` with instructions on how to start the backend, frontend, and worker processes

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed sequentially in priority order (P1 → P2 → P3) or in parallel if isolated.
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### Parallel Opportunities

- Initialization of backend (T001) and frontend (T002) can happen in parallel.
- Database (T005) and Queue (T006) setup can be done independently.
- Creation of SQLAlchemy models (T012-T015) can be done in parallel.
- API router implementation (T019-T022) can be done in parallel once the base `main.py` is established.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Ensure the scaffolding successfully launches.
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Validate schemas
4. Add User Story 3 → Test independently → Check API docs (Swagger)
5. Each story adds value without breaking previous stories