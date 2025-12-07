from pages.base_page import BasePage
from playwright.sync_api import expect

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.place_order_btn = 'a[href="/payment"]'
        self.name_card = 'input[data-qa="name-on-card"]'
        self.card_num = 'input[data-qa="card-number"]'
        self.cvc = 'input[data-qa="cvc"]'
        self.exp_month = 'input[data-qa="expiry-month"]'
        self.exp_year = 'input[data-qa="expiry-year"]'
        self.pay_btn = 'button[data-qa="pay-button"]'
        
        # Robust Selector for Success Message
        self.order_placed_header = '[data-qa="order-placed"]'

    def place_order(self, name, number, cvc, month, year):
        self.click(self.place_order_btn)
        self.type_text(self.name_card, name)
        self.type_text(self.card_num, number)
        self.type_text(self.cvc, cvc)
        self.type_text(self.exp_month, month)
        self.type_text(self.exp_year, year)
        self.click(self.pay_btn)

    def verify_success(self):
        # Increased timeout to 10s for slow CI environments
        expect(self.page.locator(self.order_placed_header)).to_be_visible(timeout=10000)