from pydantic import BaseModel
from typing import List
from app.domain.value_objects.tailored_experience import TailoredExperience

class TailoredResumeResult(BaseModel):
    """A class representing a tailored resume result."""
    summary: str
    skills: List[str]
    experiences: List[TailoredExperience]
