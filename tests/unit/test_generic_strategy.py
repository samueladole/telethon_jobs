from app.services.strategies.generic_strategy import GenericJobStrategy
from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.application_status import ApplicationStatus


class FakeBrowser:
    def open(self, url: str): pass
    def page_contains(self, text: str) -> bool: return True
    def close(self): pass


def test_generic_strategy_dry_run():
    """Test the GenericJobStrategy in dry-run mode."""
    job = JobPosting(
        id="1",
        title="Test Job",
        description="desc",
        source_url="https://example.com",
        source_channel="telegram",
    )

    strategy = GenericJobStrategy(FakeBrowser())
    result = strategy.apply(job)

    assert result.status == ApplicationStatus.DRY_RUN_SUCCESS
