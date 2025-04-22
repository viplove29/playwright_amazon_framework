from playwright.sync_api import Page
from .base_page import BasePage

class AmazonResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.results = page.locator("span.a-size-medium")

    def get_result_count(self) -> int:
        return self.results.count()
