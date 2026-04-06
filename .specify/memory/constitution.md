<!--
  Sync Impact Report:
  - Version change: N/A → 1.0.0
  - List of modified principles:
    - [PRINCIPLE_1_NAME] → I. Plan-Driven Implementation
    - [PRINCIPLE_2_NAME] → II. Rigorous Testing Discipline
    - [PRINCIPLE_3_NAME] → III. Multi-Modal Data Extraction
    - [PRINCIPLE_4_NAME] → IV. Intelligent B2B Outreach Automation
    - [PRINCIPLE_5_NAME] → V. Model-Agnostic OpenRouter Integration
  - Added sections: Technology Stack & Security, Development Workflow
  - Removed sections: None
  - Templates requiring updates:
    - ✅ .specify/templates/plan-template.md (Logic aligns with principles)
    - ✅ .specify/templates/spec-template.md (Logic aligns with principles)
    - ✅ .specify/templates/tasks-template.md (Logic aligns with principles)
    - ✅ .gemini/commands/speckit.constitution.toml (Updated outdated references)
  - Follow-up TODOs: None
-->

# Certified AI-Powered Email Assistant (TRIPLE MS) Constitution

## Core Principles

### I. Plan-Driven Implementation
All development MUST adhere strictly to the logic and phases defined in `PLAN.md`. Any divergence from the established roadmap requires a formal plan amendment and justification. This ensures structural integrity and alignment with the long-term goal of building a SaaS-ready sales engine.

### II. Rigorous Testing Discipline
A comprehensive testing strategy is mandatory. We MUST focus on empirical validation of OCR accuracy for business cards and PDFs, email generation quality (Arabic/English), and lead scoring effectiveness. "Best testing" means verifying behavioral correctness at every phase, from extraction to delivery.

### III. Multi-Modal Data Extraction
The system MUST leverage high-quality vision and text models (via OpenRouter) to extract structured company and contact information from diverse inputs, including business card images and PDF documents. Accuracy in data extraction is the foundation of the outreach engine.

### IV. Intelligent B2B Outreach Automation
Efficiency is achieved through a streamlined, end-to-end workflow: Ingest → Extract → Validate → Enrich → Score → Generate → Send → Track. The system MUST automate this pipeline while maintaining strict validation rules to ensure high-quality, professional outreach.

### V. Model-Agnostic OpenRouter Integration
To maintain flexibility and access the latest AI capabilities, the system MUST interact with AI models exclusively through OpenRouter. This decouples the application logic from specific model providers, allowing for seamless updates to Vision and Text services.

## Technology Stack & Security

The project employs a modern, modular stack:
- **Backend**: FastAPI (Python) for the core API services.
- **Frontend**: Electron + React for the desktop interface.
- **Storage**: SQLite for local persistence (SQLAlchemy ORM), with a path to PostgreSQL for SaaS scaling.
- **Security**: Sensitive credentials (OpenRouter API Keys, SMTP passwords) MUST NEVER be logged, printed, or committed to source control. Use environment variables and secure configuration management.

## Development Workflow

We follow the Spec Kit approach (Phases 0-7) to ensure a modular and scalable architecture:
- Separation of concerns between Frontend, Backend, and AI layers.
- SaaS-ready design from day one (normalized schema, API-first).
- Iterative Plan-Act-Validate cycle for every feature implementation.

## Governance

This Constitution is the foundational governing document of the project and supersedes all other documentation or practices. Amendments require a version bump and an updated Sync Impact Report. Compliance is verified through project-wide audits and the `update-agent-context.ps1` runtime guidance.

**Version**: 1.0.0 | **Ratified**: 2026-04-06 | **Last Amended**: 2026-04-06
