from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
       
        self.products_nav_btn = 'a[href="/products"]'
        self.search_input = 'input[id="search_product"]'
        self.search_btn = 'button[id="submit_search"]'
        self.view_product_btn = 'div.product-image-wrapper >> a:has-text("View Product")'
        self.add_to_cart_btn = 'button:has-text("Add to cart")'
        self.view_cart_modal_link = 'u:has-text("View Cart")' 
        self.proceed_checkout_btn = 'a:has-text("Proceed To Checkout")'

    def search_for_product(self, product_name):
       
        self.click(self.products_nav_btn)
        self.type_text(self.search_input, product_name)
        self.click(self.search_btn)

    def add_first_result_to_cart(self):
        
        self.page.locator(self.view_product_btn).first.click()
        self.click(self.add_to_cart_btn)

    def go_to_checkout(self):
        
        self.click(self.view_cart_modal_link)
        self.click(self.proceed_checkout_btn)