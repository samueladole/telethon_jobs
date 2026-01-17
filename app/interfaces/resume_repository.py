from typing import Protocol
from app.domain.entities import Resume


class ResumeRepository(Protocol):
    """Protocol for resume repository."""

    def save(self, resume: Resume, job_id: str) -> None:
        ...

    def load_base(self) -> Resume:
        ...
