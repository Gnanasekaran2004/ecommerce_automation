import pytest
import time
from pages.signup_page import LoginPage

@pytest.mark.smoke
def test_user_registration(page):
    login = LoginPage(page)
    
    login.navigate("https://automationexercise.com/")
    
    email = f"test_user_{int(time.time())}@qa.com"
    login.register_user("TestEngineer", email, "SecurePass123")
    login.delete_account()
