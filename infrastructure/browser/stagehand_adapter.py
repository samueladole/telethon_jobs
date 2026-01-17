from stagehand import Stagehand
from app.interfaces.browser_automation import BrowserAutomation
from app.domain.value_objects.form_field import FormField

class StagehandBrowser(BrowserAutomation):
    """Adapter for Stagehand browser automation."""
    def __init__(self, headless: bool = True):
        self.browser = Stagehand(
            env="LOCAL",
            headless=headless,
        )
        self.page = None

    def open(self, url: str) -> None:
        self.page = self.browser.init()
        self.page.goto(url)

    def page_contains(self, text: str) -> bool:
        return text.lower() in self.page.content().lower()

    def close(self) -> None:
        self.browser.close()

    def get_form_fields(self):
        fields = []
        for el in self.page.query_selector_all("input, textarea, select"):
            fields.append(
                FormField(
                    name=el.get_attribute("name") or "",
                    label=el.get_attribute("aria-label") or "",
                    required=el.get_attribute("required") is not None,
                    field_type=el.tag_name,
                )
            )
        return fields

    def fill_field(self, field, value):
        self.page.fill(f"[name='{field.name}']", value)

    def submit(self):
        self.page.click("button[type='submit']")
