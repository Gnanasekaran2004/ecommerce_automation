from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_login_btn = 'a[href="/login"]'
        self.name_input = 'input[data-qa="signup-name"]'
        self.email_input = 'input[data-qa="signup-email"]'
        self.signup_btn = 'button[data-qa="signup-button"]'
        
        # Registration Form
        self.gender_male = 'input[id="id_gender1"]'
        self.password = 'input[data-qa="password"]'
        self.first_name = 'input[data-qa="first_name"]'
        self.last_name = 'input[data-qa="last_name"]'
        self.address = 'input[data-qa="address"]'
        self.state = 'input[data-qa="state"]'
        self.city = 'input[data-qa="city"]'
        self.zip = 'input[data-qa="zipcode"]'
        self.mobile = 'input[data-qa="mobile_number"]'
        self.create_account_btn = 'button[data-qa="create-account"]'
        self.continue_btn = 'a[data-qa="continue-button"]'
        self.delete_account_btn = 'a[href="/delete_account"]'

    def register_user(self, name, email, password):
        self.click(self.signup_login_btn)
        self.type_text(self.name_input, name)
        self.type_text(self.email_input, email)
        self.click(self.signup_btn)
        
        # Fill details
        self.click(self.gender_male)
        self.type_text(self.password, password)
        self.type_text(self.first_name, "Gnana")
        self.type_text(self.last_name, "Sekaran")
        self.type_text(self.address, "123 Supply Chain Rd")
        self.type_text(self.state, "Tamilnadu")
        self.type_text(self.city, "Chennai")
        self.type_text(self.zip, "600001")
        self.type_text(self.mobile, "9876543210")
        
        self.click(self.create_account_btn)
        self.assert_text_visible("Account Created!")
        self.click(self.continue_btn)

    def delete_account(self):
        self.click(self.delete_account_btn)
        self.assert_text_visible("Account Deleted!")
        self.click(self.continue_btn)