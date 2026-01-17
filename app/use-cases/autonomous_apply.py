class AutonomousApply:
    def __init__(
        self,
        browser,
        form_service,
        decision_engine,
    ):
        self.browser = browser
        self.form_service = form_service
        self.decision_engine = decision_engine

    def execute(self, job, resume, match_result):
        self.browser.open(job.source_url)

        fields = self.browser.get_form_fields()
        answers = [
            self.form_service.answer(field, resume, job)
            for field in fields if field.required
        ]

        decision = self.decision_engine.decide(
            match_score=match_result.match_score,
            answer_confidences=[a.confidence for a in answers],
        )

        if not decision.should_submit:
            return decision

        for a in answers:
            self.browser.fill_field(
                next(f for f in fields if f.name == a.field_name),
                a.answer,
            )

        self.browser.submit()
        return decision
