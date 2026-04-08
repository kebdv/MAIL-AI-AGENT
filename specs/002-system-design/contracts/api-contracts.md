# API Contracts

These contracts represent the internal HTTP APIs (or function boundaries within the Modular Monolith) used to orchestrate the pipeline.

## 1. Ingestion / Extraction API

**POST** `/api/v1/ingest/document`
Initiates extraction from a business card or PDF via OpenRouter Vision.

**Request:**
```json
{
  "file_data": "base64_encoded_string",
  "mime_type": "image/jpeg",
  "source_type": "business_card"
}
```

**Response (202 Accepted - Added to Queue):**
```json
{
  "task_id": "uuid",
  "status": "pending_extraction"
}
```

## 2. Enrichment API

**POST** `/api/v1/enrich`
Triggers enrichment for a specific lead.

**Request:**
```json
{
  "lead_id": "uuid"
}
```

**Response (200 OK):**
```json
{
  "lead_id": "uuid",
  "status": "Enriched",
  "score": 85,
  "score_breakdown": {
    "industry": 30,
    "email_validity": 55
  }
}
```

## 3. AI Generation API

**POST** `/api/v1/generate-draft`
Generates an English/Arabic email draft for a qualified lead using OpenRouter Text models.

**Request:**
```json
{
  "lead_id": "uuid",
  "prompt_template_id": "uuid"
}
```

**Response (200 OK):**
```json
{
  "draft_id": "uuid",
  "subject_en": "Boosting TechFlow's Sales",
  "body_en": "...",
  "subject_ar": "تعزيز مبيعات TechFlow",
  "body_ar": "..."
}
```

## 4. Delivery API

**POST** `/api/v1/delivery/send`
Queues an approved draft for sending via standard SMTP.

**Request:**
```json
{
  "draft_id": "uuid"
}
```

**Response (202 Accepted):**
```json
{
  "interaction_log_id": "uuid",
  "status": "queued_for_delivery"
}
```
