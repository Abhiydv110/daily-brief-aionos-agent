# Daily Brief — Executive Productivity Agent

**AIONOS Agentic AI Factory — Assignment 1**

An Executive Productivity Agent that transforms scattered meetings, emails, calendars, and voice notes into a structured, trustworthy daily brief.

## Overview

Executives often receive important commitments and follow-ups across multiple sources, making it difficult to identify:

* What actions belong to them
* What actions are waiting on others
* Which deadlines have changed
* Which commitments are overdue
* Where ownership is unclear
* What has already been resolved

**Daily Brief** brings these fragmented inputs together into a unified commitment view and presents the information as a day-by-day executive brief.

## Key Capabilities

* **Commitment Identification** — Extracts actionable commitments from the supplied data pack.
* **Ownership Tracking** — Distinguishes between the executive's actions, items waiting on others, and unclear ownership.
* **Deadline Tracking** — Maintains current deadlines along with their revision history.
* **Deduplication** — Combines repeated mentions of the same commitment across different sources.
* **Status Management** — Tracks commitments as due, overdue, resolved, or unowned.
* **Evidence Trail** — Preserves the source context behind each commitment.
* **Grounded Q&A** — Provides answers through the "Ask the Agent" interface using the structured commitment records.

## Prototype Workflow

```text
Data Sources
    │
    ├── Meeting Transcript
    ├── Calendars
    ├── Email Threads
    └── Voice Notes
          │
          ▼
   Commitment Extraction
          │
          ▼
     Deduplication
          │
          ▼
   Ownership Classification
          │
          ▼
 Deadline & Status Tracking
          │
          ▼
    Daily Brief + Q&A
```

## Data Sources Represented

The prototype is based on the supplied AIONOS assignment data pack:

* 1 Leadership Sync meeting transcript
* 4 calendars
* 5 email threads
* 2 voice notes

The extracted information is represented as structured commitment records for reliable prototype execution.

## Commitment Records

The prototype demonstrates multiple commitment threads managed by a **single Executive Productivity Agent**, including:

* Vendor List → Raghav
* Q3 Campaign Deck Review
* Meridian Logistics Call
* Expense Variance Report
* Mumbai Lease Renewal

Each commitment can be evaluated using its ownership, deadline, status, evidence, and revision history.

## Architecture

The prototype follows a lightweight architecture:

```text
Data Pack
    ↓
Commitment Records
    ↓
Status & Deadline Engine
    ↓
Daily Brief Interface
    ↓
Ask the Agent
```

The prototype uses client-side/deterministic status and retrieval logic over the extracted commitment records to keep the demonstration reliable and reproducible.

## Important Assumptions

* Voice notes are treated as the executive's own statements.
* The most recently stated applicable deadline is treated as the current deadline.
* A recent resolved email can take precedence over a stale voice note.
* Ownership is not inferred when the source does not explicitly assign it.
* Lack of a reply is not treated as resolution.
* Agent responses are grounded in the structured commitment records rather than raw, unprocessed documents.

## AI Tools Used

**ChatGPT** was used during development to assist with:

* Prototype architecture
* Commitment-record structure
* Application logic
* Streamlit UI development
* Documentation
* Testing and refinement

The prototype intentionally uses deterministic retrieval and status logic over the supplied commitment records so that the demonstration remains grounded, consistent, and reproducible.

## Technologies

* Python
* Streamlit
* Structured JSON-style commitment records
* Deterministic status and deadline logic
* GitHub
* Streamlit Community Cloud

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Abhiydv110/daily-brief-aionos-agent.git
cd daily-brief-aionos-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

Then open the local URL displayed by Streamlit.

## Live Prototype

**Streamlit App:**
https://daily-brief-aionos-agent-teceryrh8watdkg32fkrgh.streamlit.app/

## Project Repository

**GitHub:**
https://github.com/Abhiydv110/daily-brief-aionos-agent

## Future Scope

The current prototype uses pre-extracted commitment records for a reliable demonstration. Future versions can extend the system with:

* Automated email ingestion
* Calendar integration
* Meeting-transcript processing
* Voice-note transcription
* LLM-based commitment extraction
* Persistent commitment storage
* Automated daily brief generation
* More advanced natural-language Q&A
* Authentication and role-based access

## Project Goal

The goal of Daily Brief is to provide an executive with a **single trusted view of commitments, ownership, deadlines, and follow-ups** instead of requiring them to manually reconcile information across multiple sources.
