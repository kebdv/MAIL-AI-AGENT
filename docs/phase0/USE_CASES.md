# Core Use Cases: End-to-End Outreach Pipeline

**Purpose**: Map the functional flow from lead ingestion to outreach tracking for the AI-Powered B2B Outreach System, using Gherkin-style scenarios.

## UC-1: Upload & Extract (Ingestion)
**Goal**: Accurately convert unstructured visual data (business cards, PDFs) into structured lead data.

```gherkin
Scenario: Successful data extraction from a clear business card
  Given the user has a clear image of a business card
  When the user uploads the image to the "Ingestion Engine"
  Then the system should trigger the OCR + Vision AI extraction
  And the system should extract the "Name", "Title", "Company", "Email", and "Phone"
  And the system should create a new Lead record with status "Extracted"

Scenario: Handling unreadable or low-resolution business cards
  Given the user has a low-resolution or blurry image of a business card
  When the user uploads the image
  Then the system should attempt OCR + Vision AI extraction
  And if the confidence score for critical fields (Name, Company) is below the threshold
  Then the system should flag the Lead record as "Manual Review Required"
  And the system should notify the user that extraction failed due to poor quality
```

## UC-2: Lead Enrichment & Scoring
**Goal**: Augment basic lead data and evaluate its potential value based on the ICP.

```gherkin
Scenario: Successful enrichment of a lead missing LinkedIn data
  Given a Lead record exists with "Company" and "Name" but no "LinkedIn Profile"
  When the "Enrichment Engine" processes the lead
  Then the system should search for the company and person on LinkedIn/Web
  And the system should update the Lead record with the discovered URL
  And the system should trigger the Lead Scoring module

Scenario: Lead Scoring based on ICP criteria
  Given a Lead record has been fully enriched
  When the "Scoring Engine" evaluates the lead
  Then the system should assign points based on:
    | Criteria | Points | Condition |
    |----------|--------|-----------|
    | Industry | 5      | Matches Construction, Data Centers, or Manufacturing |
    | Website  | 3      | Has an active corporate website |
    | Email    | 4      | Uses a professional domain (not @gmail.com) |
  And the system should update the Lead's total score
  And if the score is >= 8, mark the lead as "Qualified for Outreach"

Scenario: Handling missing email address during enrichment
  Given a Lead record lacks an "Email" address after initial extraction
  When the "Enrichment Engine" attempts to find the missing email via standard scraping patterns
  And if the email cannot be found
  Then the system should flag the Lead record as "Incomplete - Missing Email"
  And the lead should NOT proceed to the Generation phase

Scenario: Handling companies with multiple contact people or ambiguous roles
  Given a single company entity is identified during enrichment
  And multiple contacts are associated with the company (e.g., "Facilities Manager" and "Procurement Director")
  When the "Enrichment Engine" processes the contacts
  Then the system should prioritize the contact matching the Primary Persona ("Facilities/Operations Manager")
  And if roles are ambiguous, the system should queue the Lead record for "Manual Persona Assignment"
  And the system should prevent duplicate outreach to multiple contacts within the same company without manual override
```

## UC-3: AI Outreach Generation
**Goal**: Automatically draft highly personalized, bilingual emails tailored to the lead's persona and industry.

```gherkin
Scenario: Generate a personalized bilingual outreach email
  Given a Lead is "Qualified for Outreach"
  And the Lead's persona is "Facilities Manager" in the "Manufacturing" industry
  When the "Generation Engine" processes the lead
  Then it should use an AI model to draft an email
  And the draft must be bilingual (balanced Arabic/English based on detected region/name preferences)
  And the draft must specifically mention "uninterrupted power for continuous production" (Industry Pain Point)
  And the draft must include the specific CTA: "Book a Site Visit"
  And the system should save the draft for review or auto-send based on settings
```

## UC-4: Delivery & Tracking
**Goal**: Send the generated outreach and monitor lead engagement.

```gherkin
Scenario: Successful email delivery and interaction tracking
  Given an approved outreach email draft exists for a Lead
  When the system sends the email via SMTP
  Then the system should log the "Sent Date"
  And the system should update the Lead status to "Contacted"
  When the Lead replies to the email
  Then the system should log the interaction
  And the system should update the Lead status to "Replied"
  And the system should alert the sales team to follow up for the "Site Visit"
```
