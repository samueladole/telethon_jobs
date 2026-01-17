import json
from app.interfaces.llm_client import LLMClient
from app.domain.entities.resume import Resume
from app.domain.entities.job_posting import JobPosting
from app.domain.value_objects.form_answer import FormAnswer
from app.domain.value_objects.form_field import FormField


class FormAnsweringService:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def answer(self, field: FormField, resume: Resume, job: JobPosting) -> FormAnswer:
        prompt = f"""
You are filling a job application form.

Field:
Name: {field.name}
Label: {field.label}
Required: {field.required}

Resume:
{resume}

Job:
{job.title}
{job.description}

Return JSON ONLY:
{{
  "field_name": "{field.name}",
  "answer": "...",
  "confidence": 0-1
}}
"""
        raw = self.llm.complete(prompt)
        return FormAnswer(**json.loads(raw))
