class LoginPageLocatorSupplier:
    def __init__(self):
        #Locators Value
        self.email_field_locator_value ='input[name="username"]'
        self.password_field_locator_value = 'input[name="password"]'
        self.button_locator_value = "//button[contains(text(), 'Submit')]"