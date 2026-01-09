"""Filters for job postings."""

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
