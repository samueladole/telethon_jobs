from dataclasses import dataclass
from typing import List
from app.domain.value_objects.tailored_experience import TailoredExperience

@dataclass(frozen=True)
class Resume:
    """A class representing a user's resume."""
    summary: str
    skills: List[str]
    experiences: List[TailoredExperience]
