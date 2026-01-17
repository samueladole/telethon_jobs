from app.interfaces.resume_repository import ResumeRepository
from app.services.resume.resume_tailoring_service import ResumeTailoringService
from app.domain.entities.job_posting import JobPosting
from app.domain.entities.resume import Resume


class TailorResumeForJob:
    def __init__(
        self,
        repo: ResumeRepository,
        service: ResumeTailoringService,
    ):
        self.repo = repo
        self.service = service

    def execute(self, job: JobPosting) -> Resume:
        base_resume = self.repo.load_base()
        tailored = self.service.tailor(base_resume, job)
        self.repo.save(tailored, job.id)
        return tailored
