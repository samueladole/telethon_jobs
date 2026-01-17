from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.job_preference import JobPreference


class JobFilter:
    """Service to filter job postings based on user preferences."""

    def __init__(self, preference: JobPreference):
        """Initializes the JobFilter with user job preferences."""
        self.preference = preference

    def is_match(self, job: JobPosting) -> bool:
        """Checks if a job posting matches the user preferences."""
        text = f"{job.title} {job.description}".lower()

        if any(word.lower() in text for word in self.preference.excluded_keywords):
            return False

        return any(word.lower() in text for word in self.preference.required_keywords)
