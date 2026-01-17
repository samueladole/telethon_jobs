from app.domain.value_objects.application_decision import ApplicationDecision


class ApplicationDecisionEngine:
    def decide(
        self,
        match_score: float,
        answer_confidences: list[float],
        min_match: float = 0.8,
        min_answer_confidence: float = 0.75,
    ) -> ApplicationDecision:
        if match_score < min_match:
            return ApplicationDecision(False, match_score, "Low job match")

        if any(c < min_answer_confidence for c in answer_confidences):
            return ApplicationDecision(False, min(answer_confidences), "Low answer confidence")

        return ApplicationDecision(True, min(answer_confidences), "All checks passed")
