from app.services.job.job_filter import JobFilter
from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.job_preference import JobPreference

def test_job_filter_matches():
    """Test that JobFilter correctly matches a job posting based on preferences."""
    job = JobPosting(
        id="1",
        title="Python Backend Engineer",
        description="Remote job",
        source_url=None,
        source_channel="telegram",
    )

    preference = JobPreference(
        required_keywords=["python"],
        excluded_keywords=["java"],
    )

    assert JobFilter(preference).is_match(job)
