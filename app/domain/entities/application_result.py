from dataclasses import dataclass
from app.domain.value_objects.application_status import ApplicationStatus

@dataclass(frozen=True)
class ApplicationResult:
    """A class representing the result of a job application."""
    job_id: str
    status: ApplicationStatus
    reason: str
