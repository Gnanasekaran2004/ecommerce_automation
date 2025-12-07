import pytest
import time
from pages.signup_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

@pytest.mark.regression
def test_end_to_end_checkout(page):
   
    login = LoginPage(page)
    product = ProductPage(page)
    checkout = CheckoutPage(page)

    login.navigate("https://automationexercise.com/")

    email = f"buyer_{int(time.time())}@qa.com"
    login.register_user("Buyer", email, "Pass123")

    product.search_for_product("Blue Top")
    product.add_first_result_to_cart()
    product.go_to_checkout()

    checkout.place_order("VISA", "411111111111", "123", "12", "2027")
    
    checkout.verify_success()

    login.delete_account()