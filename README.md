# Daily Brief — Executive Productivity Agent

AIONOS Agentic AI Factory — Assignment 1.

## What this prototype does

It turns the supplied assignment data pack into a day-by-day executive brief.

Features:
- Monday–Friday daily tabs
- My actions
- Overdue / due-today / resolved / unowned states
- Commitment evidence
- Deadline revision history
- Deduplicated commitment records
- Grounded “Ask the Agent” panel

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL shown by Streamlit.

## Data sources represented

- Leadership Sync transcript
- 4 calendars
- 5 email threads
- 2 voice notes

## Important assumptions

- Voice notes are treated as Arjun's own statements.
- Most recently stated deadline is the current deadline.
- A recent resolved email can outrank a stale voice note.
- Ownership is never inferred when the source does not assign it.
- Lack of a reply is not treated as resolution.

## AI tools used

ChatGPT was used to help structure the prototype, logic, UI and documentation. The prototype uses deterministic retrieval/status logic over the supplied commitment records so that demo answers remain grounded and reproducible.
