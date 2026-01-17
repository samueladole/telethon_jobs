import json
from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.job_preference import JobPreference
from app.domain.value_objects.job_match_result import JobMatchResult
from app.interfaces.llm_client import LLMClient


class JobMatchingService:
    """Service to evaluate job postings against user preferences using an LLM."""

    def __init__(self, llm: LLMClient):
        self.llm = llm

    def evaluate(self, job: JobPosting, preference: JobPreference) -> JobMatchResult:
        """Evaluate a job posting against user preferences."""
        prompt = self._build_prompt(job, preference)
        raw = self.llm.complete(prompt)
        data = json.loads(raw)
        return JobMatchResult(**data)

    def _build_prompt(self, job: JobPosting, preference: JobPreference) -> str:
        return f"""
You are a job-matching engine.

Return ONLY valid JSON.

Job:
Title: {job.title}
Description: {job.description}

User Preferences:
Required keywords: {preference.required_keywords}
Excluded keywords: {preference.excluded_keywords}

Respond with:
{{
  "match_score": number between 0 and 1,
  "should_apply": boolean,
  "reason": string
}}
"""
