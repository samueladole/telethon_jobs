from dataclasses import dataclass
from typing import Dict

@dataclass
class PendingApplication:
    """A class representing a pending job application."""
    job_id: str
    job_title: str
    resume_preview: str
    answers: Dict[str, str]
    confidence: float
