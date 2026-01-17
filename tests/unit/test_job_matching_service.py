from app.services.job.job_matching_service import JobMatchingService
from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.job_preference import JobPreference

class FakeLLM:
    """A fake LLM for testing purposes."""

    def complete(self, prompt: str) -> str:
        """Return a fixed response simulating an LLM output."""

        print("LLM Prompt:", prompt)
        return """
        {
          "match_score": 0.92,
          "should_apply": true,
          "reason": "Strong Python backend role"
        }
        """

def test_job_matching_service():
    """Test the JobMatchingService with a fake LLM."""
    matcher = JobMatchingService(FakeLLM())
    result = matcher.evaluate(
        job=JobPosting(
            title="Backend Developer",
            description="Looking for a Python developer.",
            id="1",
            source_channel="TestChannel",
        ),
        preference=JobPreference(required_keywords=["python"], excluded_keywords=[]),
    )
    assert result.should_apply is True
