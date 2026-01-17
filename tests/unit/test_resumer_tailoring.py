from app.services.resume_tailoring_service import ResumeTailoringService
from app.domain.entities import Resume, Experience


class FakeLLM:
    def complete(self, _prompt: str) -> str:
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
    resume = Resume(
        summary="Engineer",
        skills=["Python"],
        experiences=[Experience("ABC", "Engineer", ["Did stuff"])],
    )

    service = ResumeTailoringService(FakeLLM())
    tailored = service.tailor(resume, job=type("J", (), {"title": "", "description": ""}))

    assert "Python" in tailored.skills
