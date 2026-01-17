from typing import Protocol
from app.domain.entities.resume import Resume

class ResumeRepository(Protocol):

    def save(self, resume: Resume, job_id: str) -> None:
        ...

    def load_base(self) -> Resume:
        ...
