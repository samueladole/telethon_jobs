class LinkedInStrategy:
    def __init__(self, browser):
        self.browser = browser

    def supports(self, job):
        return "linkedin.com/jobs" in job.source_url

    def apply(self, job):
        self.browser.open(job.source_url)

        if not self.browser.page_contains("Apply"):
            return ApplicationResult.not_supported(job.id)

        return ApplicationResult.dry_run(job.id, "LinkedIn apply detected")
