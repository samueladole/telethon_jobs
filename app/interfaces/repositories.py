from typing import Protocol
from app.domain.entities.job_posting import JobPosting

class JobRepository(Protocol):

    def save(self, job: JobPosting) -> None:
        ...
