from pydantic import BaseModel
from typing import List

class TailoredExperience(BaseModel):
    """A class representing a tailored experience for a resume."""
    company: str
    role: str
    bullets: List[str]
