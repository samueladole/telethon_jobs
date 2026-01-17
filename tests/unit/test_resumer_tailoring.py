from app.services.resume_tailoring_service import ResumeTailoringService
from app.domain.entities.resume import Resume
from app.domain.entities.job_posting import JobPosting
from app.domain.entities.experience import Experience


class FakeLLM:
    """A fake LLM client for testing purposes."""

    def complete(self, prompt: str) -> str:
        """A fake LLM client for testing purposes."""

        print("LLM Prompt:", prompt)
        return """
        {
          "summary": "Backend Python Engineer",
          "skills": ["Python", "Django"],
          "experiences": [
            {
              "company": "ABC",
              "role": "Engineer",
              "bullets": ["Built APIs"]
            }
          ]
        }
        """


def test_resume_tailoring():
    """Test the resume tailoring service."""
    resume = Resume(
        summary="Engineer",
        skills=["Python"],
        experiences=[Experience("ABC", "Engineer", ["Did stuff"])],
    )

    service = ResumeTailoringService(FakeLLM())
    tailored = service.tailor(
        resume,
        job=JobPosting(
            title="Example Job",
            description="An example job description.",
            id="1",
            source_channel="TestChannel",
        ),
    )

    assert "Python" in tailored.skills
