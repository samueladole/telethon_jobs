from app.domain.entities.application_result import ApplicationResult
from app.domain.entities.job_posting import JobPosting
from app.services.strategies.strategy_resolver import StrategyResolver


class ApplyForJob:
    def __init__(self, resolver: StrategyResolver):
        self.resolver = resolver

    def execute(self, job: JobPosting) -> ApplicationResult:
        strategy = self.resolver.resolve(job)
        return strategy.apply(job)
