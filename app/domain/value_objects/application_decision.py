from dataclasses import dataclass

@dataclass(frozen=True)
class ApplicationDecision:
    """A class representing the decision to submit a job application."""
    should_submit: bool
    confidence: float
    reason: str
