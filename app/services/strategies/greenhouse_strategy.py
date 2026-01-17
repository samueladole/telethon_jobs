class GreenhouseStrategy:
    def __init__(self, browser):
        self.browser = browser

    def supports(self, job):
        return "greenhouse.io" in job.source_url

    def apply(self, job):
        self.browser.open(job.source_url)
        return ApplicationResult.dry_run(job.id, "Greenhouse form detected")
