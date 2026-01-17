import json
from app.domain.entities.resume import Resume
from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.tailored_resume_result import TailoredResumeResult
from app.interfaces.llm_client import LLMClient


class ResumeTailoringService:
    """Service to tailor resumes for specific job postings using an LLM."""

    def __init__(self, llm: LLMClient):
        self.llm = llm

    def tailor(self, resume: Resume, job: JobPosting) -> Resume:
        """Tailor the given resume for the specified job posting."""
        prompt = self._build_prompt(resume, job)
        raw = self.llm.complete(prompt)
        data = json.loads(raw)
        tailored = TailoredResumeResult(**data)

        return Resume(
            summary=tailored.summary,
            skills=tailored.skills,
            experiences=list(exp for exp in tailored.experiences),
        )

    def _build_prompt(self, resume: Resume, job: JobPosting) -> str:
        return f"""
You are a resume optimization engine.

RULES:
- Do NOT invent experience.
- Rephrase bullets only.
- Keep facts identical.
- Return VALID JSON ONLY.

Job:
{job.title}
{job.description}

Resume:
Summary: {resume.summary}
Skills: {resume.skills}
Experience:
{
            [
                {"company": e.company, "role": e.role, "bullets": e.bullets}
                for e in resume.experiences
            ]
        }

Respond with:
{{
  "summary": "...",
  "skills": [...],
  "experiences": [
    {{
      "company": "...",
      "role": "...",
      "bullets": [...]
    }}
  ]
}}
"""
