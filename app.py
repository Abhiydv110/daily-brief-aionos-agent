
import streamlit as st
from datetime import date

st.set_page_config(page_title="Daily Brief | Executive Productivity Agent", page_icon="📋", layout="wide")

# -----------------------------
# Data pack: based on assignment PPT
# -----------------------------
COMMITMENTS = [
    {
        "id": "C1",
        "title": "Vendor list to Raghav",
        "category": "Mine",
        "counterparty": "Raghav",
        "source": "Leadership Sync + Vendor List emails + Voice Note 1",
        "deadline_history": [
            ("Mon 21 Sep", "Tue EOD"),
            ("Tue 22 Sep", "Tue morning"),
            ("Tue 22 Sep", "Wed morning"),
        ],
        "current_deadline": "Wed morning",
        "deadline_day": "Wed",
        "status_by_day": {
            "Mon": "Open", "Tue": "Open", "Wed": "Overdue",
            "Thu": "Overdue", "Fri": "Overdue"
        },
        "resolution": "No message confirms it was sent.",
        "evidence": "By Wednesday 8:45 AM, Raghav is still checking in.",
        "keywords": ["vendor", "raghav", "list"]
    },
    {
        "id": "C2",
        "title": "Q3 campaign deck review",
        "category": "Mine",
        "counterparty": "Leadership team",
        "source": "Q3 Campaign Deck email thread + Calendar",
        "deadline_history": [
            ("Mon 21 Sep", "Wed"),
            ("Wed 23 Sep", "Thu 9:30 AM"),
        ],
        "current_deadline": "Thu 9:30 AM",
        "deadline_day": "Thu",
        "status_by_day": {
            "Mon": "Open", "Tue": "Open", "Wed": "Open",
            "Thu": "Due today", "Fri": "Open"
        },
        "resolution": "Review date moved from Wednesday to Thursday 9:30 AM.",
        "evidence": "Calendar confirms the Thursday deck-review conflict.",
        "keywords": ["q3", "campaign", "deck", "review"]
    },
    {
        "id": "C3",
        "title": "Meridian Logistics call",
        "category": "Mine",
        "counterparty": "Meridian Logistics",
        "source": "Call Reschedule email thread + Calendar + Voice Note 2",
        "deadline_history": [
            ("Tue 22 Sep", "Wed 3 PM"),
        ],
        "current_deadline": "Wed 3 PM",
        "deadline_day": "Wed",
        "status_by_day": {
            "Mon": "Open", "Tue": "Open", "Wed": "Resolved",
            "Thu": "Resolved", "Fri": "Resolved"
        },
        "resolution": "Call confirmed for Wednesday 3 PM.",
        "evidence": "A more recent resolved email outranks the stale voice-note reminder.",
        "keywords": ["meridian", "logistics", "call"]
    },
    {
        "id": "C4",
        "title": "Expense variance report",
        "category": "Mine",
        "counterparty": "Finance",
        "source": "Expense Variance Report email thread + Voice Note 2",
        "deadline_history": [
            ("Mon 21 Sep", "Thu morning"),
            ("Wed 23 Sep", "Wed evening"),
        ],
        "current_deadline": "Wed evening",
        "deadline_day": "Wed",
        "status_by_day": {
            "Mon": "Open", "Tue": "Open", "Wed": "Due today",
            "Thu": "Overdue", "Fri": "Overdue"
        },
        "resolution": "Deadline was pulled in from Thursday morning to Wednesday evening.",
        "evidence": "Email update is more recent than the partly stale voice note.",
        "keywords": ["expense", "variance", "report", "finance"]
    },
    {
        "id": "C5",
        "title": "Mumbai lease sign-off",
        "category": "Unowned",
        "counterparty": "Unclear",
        "source": "Leadership Sync + Mumbai Lease Renewal emails",
        "deadline_history": [
            ("Mon 21 Sep", "Friday"),
        ],
        "current_deadline": "Friday",
        "deadline_day": "Fri",
        "status_by_day": {
            "Mon": "Unowned", "Tue": "Unowned", "Wed": "Unowned",
            "Thu": "Unowned", "Fri": "Due today"
        },
        "resolution": "No owner assigned.",
        "evidence": "Two Facilities-wide reminders went out, but no owner was assigned.",
        "keywords": ["mumbai", "lease", "sign-off", "facilities"]
    },
]

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]

def badge(status):
    mapping = {
        "Overdue": "🔴",
        "Due today": "🟠",
        "Resolved": "🟢",
        "Unowned": "🟣",
        "Open": "🔵",
    }
    return f"{mapping.get(status, '⚪')} {status}"

def records_for_day(day):
    return [(c, c["status_by_day"][day]) for c in COMMITMENTS]

def answer_question(question, day):
    q = question.lower().strip()
    records = records_for_day(day)

    if not q:
        return "Ask something like: “What is overdue?”, “Who am I waiting on?”, or “What is unowned?”"

    # Intent detection
    if any(x in q for x in ["overdue", "late", "past due"]):
        items = [(c, s) for c, s in records if s == "Overdue"]
        if not items:
            return f"No commitment is marked overdue on {day}."
        return "### Overdue\n" + "\n".join(
            f"- **{c['title']}** — deadline: {c['current_deadline']}. {c['evidence']}"
            for c, _ in items
        )

    if any(x in q for x in ["unowned", "no owner", "owner"]):
        items = [(c, s) for c, s in records if c["category"] == "Unowned"]
        return "### Unclear ownership\n" + "\n".join(
            f"- **{c['title']}** — owner: **Unclear**. The agent does not guess; {c['evidence']}"
            for c, _ in items
        )

    if any(x in q for x in ["waiting", "others", "someone else", "counterparty"]):
        items = [(c, s) for c, s in records if c["category"] != "Mine" or c["counterparty"] != "Unclear"]
        # Keep answer useful from Arjun's perspective
        return "### From Arjun's point of view\nNo separate waiting-on-others record is explicitly assigned in the supplied data pack. The Mumbai lease is **unowned**, not automatically assigned to Facilities."

    if any(x in q for x in ["today", "due"]):
        items = [(c, s) for c, s in records if s == "Due today"]
        if not items:
            return f"Nothing is marked due today on {day}."
        return "### Due today\n" + "\n".join(
            f"- **{c['title']}** — {c['current_deadline']}"
            for c, _ in items
        )

    if any(x in q for x in ["resolved", "done", "complete"]):
        items = [(c, s) for c, s in records if s == "Resolved"]
        if not items:
            return f"No commitment is marked resolved on {day}."
        return "### Resolved\n" + "\n".join(f"- **{c['title']}** — {c['resolution']}" for c, _ in items)

    # Keyword retrieval
    matches = []
    for c, s in records:
        if any(k in q for k in c["keywords"]) or any(k in q for k in c["title"].lower().split()):
            matches.append((c, s))
    if matches:
        return "### Matching records\n" + "\n".join(
            f"- **{c['title']}** — {badge(s)} — deadline: {c['current_deadline']}. {c['resolution']}"
            for c, s in matches
        )

    return (
        "I could not find a grounded answer in the commitment records. "
        "Try asking about **overdue items, today's deadlines, resolved items, "
        "unowned work, vendor list, Q3 deck, Meridian call, expense report, or Mumbai lease**."
    )

# -----------------------------
# UI
# -----------------------------
st.title("📋 Daily Brief")
st.caption("An Executive Productivity Agent • AIONOS Assignment 1")
st.markdown("**Purpose:** turn scattered meetings, calendars, email threads and voice notes into one trusted daily brief.")

with st.sidebar:
    st.header("Data Pack")
    st.write("1 meeting transcript")
    st.write("4 calendars")
    st.write("5 email threads")
    st.write("2 voice notes")
    st.divider()
    st.write("**Grounding rule:** the agent does not guess missing ownership or resolution.")

tabs = st.tabs(DAYS)

for tab, day in zip(tabs, DAYS):
    with tab:
        records = records_for_day(day)
        overdue = sum(s == "Overdue" for _, s in records)
        due = sum(s == "Due today" for _, s in records)
        unowned = sum(c["category"] == "Unowned" for c, _ in records)
        resolved = sum(s == "Resolved" for _, s in records)

        st.subheader(f"{day} • Daily Brief")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Overdue", overdue)
        m2.metric("Due today", due)
        m3.metric("Unowned", unowned)
        m4.metric("Resolved", resolved)

        st.divider()

        mine = [(c, s) for c, s in records if c["category"] == "Mine"]
        unowned_items = [(c, s) for c, s in records if c["category"] == "Unowned"]

        st.markdown("### My actions")
        for c, s in mine:
            st.markdown(
                f"**{badge(s)} — {c['title']}**  \n"
                f"Counterparty: {c['counterparty']} • Current deadline: **{c['current_deadline']}**  \n"
                f"Source: {c['source']}"
            )

        st.markdown("### Ownership gaps")
        for c, s in unowned_items:
            st.warning(
                f"**{c['title']}** — owner: **Unclear**. "
                "The agent surfaces the gap instead of assigning someone automatically."
            )

        with st.expander("View commitment evidence & deadline history"):
            for c, s in records:
                st.markdown(f"#### {c['title']} — {badge(s)}")
                st.write(f"**Evidence:** {c['evidence']}")
                st.write(f"**Resolution:** {c['resolution']}")
                st.write("**Deadline history:**")
                for d, deadline in c["deadline_history"]:
                    st.write(f"- {d} → {deadline}")

st.divider()

st.header("🤖 Ask the Agent")
st.caption("Answers are grounded only in the extracted commitment records shown above.")

question = st.text_input(
    "Ask about the week",
    placeholder="e.g. What is overdue? Who has no owner? What happened to the vendor list?"
)
selected_day = st.selectbox("View from day", DAYS, index=2)

if st.button("Ask", type="primary"):
    st.markdown(answer_question(question, selected_day))

st.divider()
st.subheader("Architecture")
st.code(
    "Raw inputs → Extract commitments → Deduplicate → Classify → Track deadlines → Daily Brief + Q&A",
    language="text"
)
st.caption("Prototype note: the supplied assignment data is pre-extracted into commitment records so the 6-hour prototype remains reliable and demoable.")
