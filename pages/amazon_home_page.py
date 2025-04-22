from playwright.sync_api import Page
from .base_page import BasePage

class AmazonHomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_box = page.locator("input#twotabsearchtextbox")
        self.search_button = page.locator("input#nav-search-submit-button")

    def load(self):
        self.navigate("https://www.amazon.in")

    def search_product(self, product_name: str):
        self.search_box.fill(product_name)
        self.search_button.click()
