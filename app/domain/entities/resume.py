from dataclasses import dataclass
from typing import List
from app.domain.entities.experience import Experience

@dataclass(frozen=True)
class Resume:
    """A class representing a user's resume."""
    summary: str
    skills: List[str]
    experiences: List[Experience]
