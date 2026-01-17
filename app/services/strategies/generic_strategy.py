from app.domain.entities.application_result import ApplicationResult
from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.application_status import ApplicationStatus
from app.interfaces.application_strategy import ApplicationStrategy
from app.interfaces.browser_automation import BrowserAutomation


class GenericJobStrategy(ApplicationStrategy):
    """A generic job application strategy that attempts to identify application flows on job posting pages."""

    def __init__(self, browser: BrowserAutomation):
        self.browser = browser

    def supports(self, job: JobPosting) -> bool:
        return job.source_url is not None

    def apply(self, job: JobPosting) -> ApplicationResult:
        if not job.source_url:
            return ApplicationResult(
                job_id=job.id,
                status=ApplicationStatus.NOT_SUPPORTED,
                reason="No source URL provided",
            )
        self.browser.open(job.source_url)

        if self.browser.page_contains("apply"):
            return ApplicationResult(
                job_id=job.id,
                status=ApplicationStatus.DRY_RUN_SUCCESS,
                reason="Apply button detected",
            )

        return ApplicationResult(
            job_id=job.id,
            status=ApplicationStatus.NOT_SUPPORTED,
            reason="No apply flow detected",
        )
