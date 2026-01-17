from pydantic import BaseModel

class FormAnswer(BaseModel):
    """A class representing an answer to a form field."""
    field_name: str
    answer: str
    confidence: float
