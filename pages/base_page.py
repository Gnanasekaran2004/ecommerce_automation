from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.locator(selector).first.wait_for()
        self.page.locator(selector).first.click()

    def type_text(self, selector, text):
        self.page.locator(selector).first.fill(text)

    def assert_text_visible(self, text):
        expect(self.page.get_by_text(text).first).to_be_visible()
