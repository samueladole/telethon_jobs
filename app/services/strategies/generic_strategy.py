from app.domain.entities import ApplicationResult, JobPosting
from app.domain.value_objects import ApplicationStatus
from app.services.application_strategy import ApplicationStrategy
from app.interfaces.browser_automation import BrowserAutomation


class GenericJobStrategy(ApplicationStrategy):
    def __init__(self, browser: BrowserAutomation):
        self.browser = browser

    def supports(self, job: JobPosting) -> bool:
        return job.source_url is not None

    def apply(self, job: JobPosting) -> ApplicationResult:
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
