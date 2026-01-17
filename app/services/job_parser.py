"""Service to parse job postings from messages."""
import re
from typing import Optional
from app.domain.entities.job_posting import JobPosting


class JobParser:
    """Service to parse job postings from messages."""

    def parse(self, message: str) -> Optional[JobPosting]:
        """Parses a job posting from a message string."""
        url_match = re.search(r"https?://\S+", message)
        if not url_match:
            return None

        return JobPosting(
            id=str(hash(message)),
            title=message[:80],
            description=message,
            source_url=url_match.group(0),
            source_channel="telegram",
        )
