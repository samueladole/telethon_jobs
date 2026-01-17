from app.domain.entities import JobPosting, ApplicationResult
from app.services.strategy_resolver import StrategyResolver


class ApplyForJob:
    def __init__(self, resolver: StrategyResolver):
        self.resolver = resolver

    def execute(self, job: JobPosting) -> ApplicationResult:
        strategy = self.resolver.resolve(job)
        return strategy.apply(job)
