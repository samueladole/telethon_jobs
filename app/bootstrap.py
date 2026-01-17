from typing import Any, Dict

from app.services.application_decision_engine import ApplicationDecisionEngine
from app.services.form_answering_service import FormAnsweringService
from app.services.job.job_matching_service import JobMatchingService
from app.services.llm_factory import create_llm
from app.services.resume.resume_tailoring_service import ResumeTailoringService
from app.services.strategies.generic_strategy import GenericJobStrategy
from app.services.strategies.greenhouse_strategy import GreenhouseStrategy
from app.services.strategies.linkedin_strategy import LinkedInStrategy
from app.services.strategies.strategy_resolver import StrategyResolver
from infrastructure.browser.stagehand_adapter import StagehandBrowser


def build_container(config: Dict[str, Any]) -> Dict[str, Any]:
    """Builds the dependency injection container."""

    llm = create_llm(config["llm"])

    browser = StagehandBrowser(headless=True)

    strategies = StrategyResolver([
        LinkedInStrategy(browser),
        GreenhouseStrategy(browser),
        GenericJobStrategy(browser),
    ])

    return {
        "llm": llm,
        "matcher": JobMatchingService(llm),
        "resume_tailor": ResumeTailoringService(llm),
        "form_service": FormAnsweringService(llm),
        "decision_engine": ApplicationDecisionEngine(),
        "browser": browser,
        "strategies": strategies,
    }
