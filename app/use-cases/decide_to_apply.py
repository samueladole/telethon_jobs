from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.job_preference import JobPreference
from app.services.job.job_matching_service import JobMatchingService


class DecideToApply:
    def __init__(self, matcher: JobMatchingService):
        self.matcher = matcher

    def execute(self, job: JobPosting, preference: JobPreference) -> bool:
        result = self.matcher.evaluate(job, preference)
        return result.should_apply
