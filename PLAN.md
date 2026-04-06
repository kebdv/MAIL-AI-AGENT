# AI-Powered B2B Sales Engine (TRIPLE MS)

## Executive Summary

This project is a **local-first AI-powered B2B outreach system** designed for TRIPLE MS, a company specializing in **large-scale diesel generators and power solutions**.

The system automates the full outreach pipeline:

* Extracting structured data from business cards and PDFs
* Enriching company information
* Generating highly personalized bilingual (Arabic/English) sales emails
* Sending emails via SMTP
* Tracking interactions and maintaining full company history locally

The architecture is **SaaS-ready**, meaning it is designed from the beginning to scale into a cloud-based product while initially running on a local machine using SQLite.

The system acts as an **AI Sales Engine**, not just an assistant, with a focus on:

* Conversion-driven outreach
* Automation with strict validation rules
* Structured data and tracking

---

# System Vision

A modular, scalable, and production-ready system that:

* Operates locally for personal use
* Separates frontend, backend, and AI layers
* Can be migrated to cloud infrastructure with minimal refactoring

---

# Core Capabilities

1. Business Card & PDF Processing (OCR + Understanding)
2. Contact & Company Data Extraction
3. Lead Enrichment (optional but supported)
4. Intelligent Lead Scoring
5. Hybrid AI Email Generation (Template + Personalization)
6. Automated Email Sending (SMTP)
7. Email Tracking & Interaction History
8. Optional Follow-up System

---

# Architecture Overview

```
Desktop App (Frontend)
        ↓
Local Backend API (FastAPI)
        ↓
---------------------------------
| AI Services (OpenRouter APIs) |
| Email Service (SMTP)         |
| SQLite Database             |
---------------------------------
```

---

# Technology Stack

## Backend

* FastAPI (Python)
* SQLite (initial)
* SQLAlchemy ORM

## AI Models

* Vision: Qwen3 VL 235B (via OpenRouter)
* Text: Qwen3.6 Plus Preview (via OpenRouter)

## Email

* SMTP (Gmail or custom provider)

## Frontend (Desktop)

* Electron + React (recommended)

---

# Development Phases (Spec Kit Approach)

---

## Phase 0 — Product Specification

### Objective

Define the business logic, target users, and value proposition.

### Outputs

* Use cases
* ICP (Ideal Customer Profile)
* Success metrics

### Key Use Cases

* Upload business card or PDF
* Extract company/contact data
* Auto-find missing email
* Generate personalized email
* Send and track emails

---

## Phase 1 — System Design

### Objective

Design a modular, scalable architecture.

### Components

* Ingestion Service
* AI Service
* Lead Service
* Email Service
* Database Service

### Requirements

* Clear separation of concerns
* API-first design
* SaaS-ready structure

---

## Phase 2 — Database Design

### Objective

Design a structured and scalable data model.

### Core Tables

* companies
* contacts
* leads
* emails
* followups (optional)

### Requirements

* Normalized schema
* Support tracking and history
* Easy migration to PostgreSQL later

---

## Phase 3 — AI Capabilities

### Objective

Define all AI-powered features.

### Components

1. OCR & Document Understanding
2. Entity Extraction (structured JSON)
3. Email Generation (Hybrid approach)
4. Language Detection (Arabic / English)

### Strategy

* Template-based emails + AI personalization
* Strict output formatting (JSON)

---

## Phase 4 — Agent Logic

### Objective

Define system behavior and decision-making.

### Flow

```
Input → Extract → Validate → Enrich → Score → Generate → Send → Track
```

### Key Features

* Auto-approval rules (no manual review required)
* Lead scoring system
* Smart handling of missing data

---

## Phase 5 — Email System

### Objective

Enable reliable email delivery and tracking.

### Features

* SMTP sending
* Email status tracking
* Reply detection (basic)

### Notes

* Open tracking requires pixel tracking (optional future enhancement)

---

## Phase 6 — Desktop Interface

### Objective

Provide a simple and efficient user interface.

### Features

* Upload interface
* Leads dashboard
* Email status tracking
* Manual override (optional)

### Requirement

* Frontend fully separated from backend

---

## Phase 7 — Testing & Optimization

### Objective

Improve system performance and accuracy.

### Focus Areas

* OCR accuracy
* Email quality
* Conversion rate
* Lead scoring effectiveness

---

# Lead Scoring System

Example scoring model:

| Factor             | Score |
| ------------------ | ----- |
| Industrial company | +5    |
| Has website        | +3    |
| Corporate email    | +4    |
| Relevant industry  | +5    |

### Purpose

Prioritize high-value leads and improve email personalization.

---

# Email Strategy

## Hybrid Model

* Fixed template structure
* AI fills dynamic fields

## Goals

* Increase reply rate
* Encourage call booking
* Maintain professional tone

---

# Future Roadmap (SaaS Transition)

* Replace SQLite with PostgreSQL
* Add authentication & multi-user support
* Deploy backend (AWS / VPS)
* Convert desktop app to web dashboard
* Add analytics dashboard

---

# Final Notes

This system is designed to:

* Start as a personal productivity tool
* Evolve into a scalable SaaS product
* Focus on real business outcomes (replies, calls, deals)

The success of this project depends not only on automation, but on:

* Data quality
* Email strategy
* Targeting accuracy

---

**End of Document**
