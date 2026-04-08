# Data Model

## Entities

### Lead
The core prospect extracted and enriched by the system.
- `id` (UUID, Primary Key)
- `company_id` (UUID, Foreign Key)
- `first_name` (String, Nullable)
- `last_name` (String, Nullable)
- `job_title` (String, Nullable)
- `email` (String, Unique, Nullable)
- `phone` (String, Nullable)
- `status` (Enum: Extracted, Enriched, Qualified, Contacted, Replied, Failed)
- `score` (Integer)
- `score_breakdown` (JSON - tracks Industry, Website, Email scores)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

### Company
The organization a Lead belongs to.
- `id` (UUID, Primary Key)
- `name` (String)
- `domain` (String, Unique, Nullable)
- `industry` (String, Nullable)
- `size` (String, Nullable)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

### OutreachDraft
The AI-generated email content for a Lead.
- `id` (UUID, Primary Key)
- `lead_id` (UUID, Foreign Key)
- `subject_en` (String)
- `body_en` (Text)
- `subject_ar` (String)
- `body_ar` (Text)
- `prompt_template_used` (String)
- `status` (Enum: Draft, Approved, Sent, Rejected)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

### InteractionLog
Tracking events related to delivery and engagement.
- `id` (UUID, Primary Key)
- `lead_id` (UUID, Foreign Key)
- `event_type` (Enum: Sent, Delivered, Opened, Replied, Bounced)
- `event_date` (Timestamp)
- `metadata` (JSON - e.g. reply text, bounce reason)

### SystemPrompt
Dynamic storage for prompt templates.
- `id` (UUID, Primary Key)
- `name` (String, Unique)
- `content_english_logic` (Text)
- `is_active` (Boolean)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

## Relationships
- A `Company` has many `Leads` (1:N)
- A `Lead` has many `OutreachDrafts` (1:N, typically 1 active)
- A `Lead` has many `InteractionLogs` (1:N)
