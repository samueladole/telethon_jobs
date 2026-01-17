from pydantic import BaseModel, Field

class JobMatchResult(BaseModel):
    """A class representing the result of a job matching process."""
    match_score: float = Field(ge=0.0, le=1.0)
    should_apply: bool
    reason: str
