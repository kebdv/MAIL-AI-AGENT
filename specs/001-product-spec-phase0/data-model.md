# Data Model: Product Specification Phase 0

This document defines the business entities and data structures required for the Phase 0 Product Specification.

## Ideal Customer Profile (ICP)

- **Region**: GCC Countries (Saudi Arabia, UAE, Qatar, Kuwait, Bahrain, Oman).
- **Target Industries**:
  - Construction & Infrastructure
  - Industrial Manufacturing
  - Logistics & Warehousing
- **Target Persona**: Facilities Manager, Operations Manager, Maintenance Manager.
- **Pain Points**: Power reliability, generator maintenance costs, emergency backup needs.
- **Power Requirement**: 50kVA to 2000kVA (Large-scale).

## Use Case: End-to-End Outreach Pipeline

### UC-1: Ingestion & Extraction
1. **Input**: Business card image or PDF document.
2. **Action**: OCR + Vision AI extraction.
3. **Data**: Name, Title, Company, Email, Phone, Website.

### UC-2: Lead Enrichment & Scoring
1. **Input**: Extracted company name.
2. **Action**: Search for website/LinkedIn (if missing).
3. **Scoring**: Industry relevance (5 pts), Website presence (3 pts), Professional email (4 pts).

### UC-3: AI Outreach Generation
1. **Action**: Generate bilingual email (Arabic/English).
2. **Personalization**: Mention industry + specific persona pain points.
3. **Call-to-Action**: Book Site Visit.

### UC-4: Delivery & Tracking
1. **Action**: Send via SMTP.
2. **Tracking**: Log date, status, and lead interaction.

## Success Metrics

- **Data Accuracy**: % of correct extractions verified manually.
- **Reply Rate**: % of outreach emails receiving a response.
- **Conversion (Meetings)**: % of leads booking a site visit/consultation.
