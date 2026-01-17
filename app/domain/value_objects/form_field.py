from dataclasses import dataclass

@dataclass(frozen=True)
class FormField:
    """A class representing a form field required for job application."""
    name: str
    label: str
    required: bool
    field_type: str  # text, textarea, select, checkbox
