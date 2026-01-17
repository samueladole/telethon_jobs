from typing import Protocol
from app.domain.entities.application_result import ApplicationResult
from app.domain.entities.job_posting import JobPosting


class ApplicationStrategy(Protocol):
    def supports(self, job: JobPosting) -> bool:
        ...

    def apply(self, job: JobPosting) -> ApplicationResult:
        ...
