from app.domain.entities import JobPosting
from app.domain.value_objects.job_preference import JobPreference
from app.interfaces.telegram_client import TelegramClient
from app.interfaces.repositories import JobRepository
from app.services.job_parser import JobParser
from app.services.job_filter import JobFilter


class ListenForJobs:
    """Listens for job postings from a Telegram channel and processes them."""

    def __init__(
        self,
        telegram_client: TelegramClient,
        job_repository: JobRepository,
        job_parser: JobParser,
        job_filter: JobFilter,
    ):
        self.telegram_client = telegram_client
        self.job_repository = job_repository
        self.job_parser = job_parser
        self.job_filter = job_filter

    def start(self) -> None:
        self.telegram_client.listen(self._handle_message)

    def _handle_message(self, message: str) -> None:
        job = self.job_parser.parse(message)
        if not job:
            return

        if self.job_filter.is_match(job):
            self.job_repository.save(job)
