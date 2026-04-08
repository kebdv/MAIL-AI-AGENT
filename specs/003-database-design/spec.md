# Feature Specification: Database Design

**Feature Branch**: `003-database-design`  
**Created**: 2026-04-08  
**Status**: Draft  
**Input**: User description: "Phase 2 — Database Design"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Relational Persistence for Lead Pipeline (Priority: P1)

As a System Backend, I need a robust and persistent data store for Leads, Companies, and Outreach Drafts, so that the AI agent can safely track the state of every prospect from ingestion to delivery without data loss.

**Why this priority**: Without a functional persistence layer mapped cleanly to the pipeline states, the core outreach automation engine cannot operate across multiple asynchronous stages (e.g., OCR, Enrichment, Generation).

**Independent Test**: Can be fully tested by creating, reading, updating, and deleting Lead and Company records through a generic interface or script, confirming that relations are maintained.

**Acceptance Scenarios**:

1. **Given** an extracted business card, **When** the system saves the Lead, **Then** the record is persisted with a status of `Extracted` and linked to its corresponding Company.
2. **Given** a Lead undergoing enrichment, **When** the AI engine returns a score, **Then** the Lead record is updated with the integer score and detailed JSON breakdown.

---

### User Story 2 - Transactional Safety & Dead Letter Recovery (Priority: P2)

As a System Operator, I need failed asynchronous tasks to be safely captured in the database alongside interaction logs, so that I can manually review errors, retry failed tasks, and audit email delivery events (sent, bounced, replied).

**Why this priority**: Reliability is paramount. Unhandled errors during LLM generation or SMTP delivery must not result in lost leads.

**Independent Test**: Can be fully tested by simulating an API failure (e.g., OpenRouter timeout) and verifying that the original task payload is securely stored in a Dead Letter Queue (DLQ) table.

**Acceptance Scenarios**:

1. **Given** a background task that fails three times, **When** the system captures the failure, **Then** a new record is created in the Dead Letter table containing the function name, arguments, and stack trace.
2. **Given** an email delivery event via SMTP, **When** the email bounces, **Then** an InteractionLog record is created linking the bounce event to the specific Lead.

---

### User Story 3 - Dynamic Configuration & Prompt Storage (Priority: P3)

As an AI Administrator, I need the ability to store, update, and toggle bilingual system prompts within the database, so that I can adjust the AI's behavior without deploying new code.

**Why this priority**: Decoupling the LLM prompt instructions from the application logic ensures the sales team can rapidly iterate on Arabic/English email templates.

**Independent Test**: Can be fully tested by querying the active system prompt, updating its contents in the database, and retrieving the updated prompt.

**Acceptance Scenarios**:

1. **Given** multiple system prompts for generation, **When** the generation engine requests a prompt, **Then** only the template flagged as `is_active=True` is returned.

---

### Edge Cases

- What happens if two background workers attempt to update the same Lead simultaneously (e.g., score enrichment and email generation)?
- How does the system handle schema migrations if new data columns (like LinkedIn URL) are needed for Leads later on?
- How are string encodings (specifically Arabic text) persisted to ensure no data corruption?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The Database MUST persistently store Leads, Companies, Outreach Drafts, Interaction Logs, System Prompts, and Dead Letter Queue items.
- **FR-002**: The Database MUST enforce foreign key relationships (e.g., preventing the deletion of a Company if Leads are still attached to it).
- **FR-003**: The Database MUST support structured JSON storage for complex, semi-structured outputs like scoring breakdowns and AI metadata.
- **FR-004**: The Database MUST safely handle unicode/UTF-8 strings natively to support complex Arabic character storage without mojibake.
- **FR-005**: The Database MUST provide a mechanism for safely upgrading the schema over time (migrations).

### Key Entities

- **Lead**: Represents a prospect, storing basic details (Name, Email, Job Title), computed scores, and the current pipeline status.
- **Company**: Represents an organization, linked to one or more Leads.
- **OutreachDraft**: Stores the generated English and Arabic email text tied to a specific Lead.
- **InteractionLog**: An immutable ledger of events (Sent, Bounced, Opened, Replied) mapped to Leads.
- **SystemPrompt**: Stores the model instructions dynamically.
- **DeadLetter**: Captures failed asynchronous background tasks to prevent data loss.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of pipeline state transitions (Ingest -> Extract -> Enrich -> Score -> Generate -> Send) map correctly to a database record update.
- **SC-002**: Database allows safe storage and retrieval of complex Arabic characters (UTF-8) with 0% data corruption.
- **SC-003**: Database locks or handles concurrent writes from the background queue without deadlocking or losing state updates.
- **SC-004**: A complete schema migration can be generated and applied from a clean state to production-ready in under 1 minute.

## Assumptions

- The database will utilize a robust ORM layer (like SQLAlchemy) to interact with the underlying data store, as established in Phase 1.
- Initial scaling is strictly local (desktop), so SQLite is sufficient and is assumed to be the target engine, with standard constraints configured.
- Security and encryption of rest data (e.g., database file encryption) are handled outside the scope of this specific table schema design.