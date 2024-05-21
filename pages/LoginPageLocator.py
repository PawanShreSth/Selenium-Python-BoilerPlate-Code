class LoginPageLocatorSupplier:
    def __init__(self):
        #Locators Value for login_test.py
        self.email_field_locator_value ='input[name="username"]'
        self.password_field_locator_value = 'input[name="password"]'
        self.button_locator_value = "//button[contains(text(), 'Submit')]"

        #Locators value for login2_test.py"]'
        self.button_locator_value_2 = "button[type='submit']"