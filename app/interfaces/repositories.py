from typing import Protocol
from app.domain.entities import JobPosting


class JobRepository(Protocol):
    """Protocol for job posting repository."""

    def save(self, job: JobPosting) -> None:
        """Saves a job posting to the repository."""
