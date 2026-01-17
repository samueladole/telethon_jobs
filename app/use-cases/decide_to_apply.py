from app.domain.entities import JobPosting
from app.domain.value_objects import JobPreference
from app.services.job_matching_service import JobMatchingService


class DecideToApply:
    def __init__(self, matcher: JobMatchingService):
        self.matcher = matcher

    def execute(self, job: JobPosting, preference: JobPreference) -> bool:
        result = self.matcher.evaluate(job, preference)
        return result.should_apply
