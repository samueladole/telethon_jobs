from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Experience:
    """A class representing a work experience entry."""
    company: str
    role: str
    bullets: List[str]
