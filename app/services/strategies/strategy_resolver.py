from typing import List
from app.domain.entities.job_posting import JobPosting
from app.interfaces.application_strategy import ApplicationStrategy


class StrategyResolver:
    """Resolves the appropriate application strategy for a given job posting."""

    def __init__(self, strategies: List[ApplicationStrategy]):
        self.strategies = strategies

    def resolve(self, job: JobPosting) -> ApplicationStrategy:
        """Resolves the appropriate application strategy for the given job posting."""
        for strategy in self.strategies:
            if strategy.supports(job):
                return strategy
        raise RuntimeError("No application strategy found")
