from app.services.job_matching_service import JobMatchingService
from app.domain.value_objects import JobMatchResult


class FakeLLM:
    def complete(self, prompt: str) -> str:
        return """
        {
          "match_score": 0.92,
          "should_apply": true,
          "reason": "Strong Python backend role"
        }
        """


def test_job_matching_service():
    matcher = JobMatchingService(FakeLLM())
    result = matcher.evaluate(
        job=type("J", (), {"title": "Python Dev", "description": "Backend work"}),
        preference=type("P", (), {"required_keywords": ["python"], "excluded_keywords": []}),
    )
    assert result.should_apply is True
