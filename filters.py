"""Filters for job postings."""
import datetime
import re

KEYWORDS = [
"developer",
"software engineer",
"backend",
"frontend",
"python",
"javascript",
"node",
"react",
"data analyst",
"data scientist",
"machine learning"
]

def is_relevant(text: str) -> bool:
    """Check if the text contains any relevant keywords."""
    text = text.lower()
    return any(keyword in text for keyword in KEYWORDS)

def extract_apply_link(text: str) -> str | None:
    """Extract the first URL from the text."""
    match = re.search(r"https?://\S+", text)
    return match.group(0) if match else None

def contains_remote_option(text: str) -> bool:
    """Check if the job posting mentions remote work options."""
    text = text.lower()
    remote_keywords = ["remote", "work from home", "telecommute", "distributed team"]
    return any(keyword in text for keyword in remote_keywords)

def get_offset_date(days: int = 7) -> datetime.datetime:
    """Get the offset date for filtering old messages."""
    return datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(days=days)
