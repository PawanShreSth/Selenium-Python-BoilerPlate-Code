class RadioButtonHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def select_radio_button(self, locator):
        self.driver.find_element(*locator).click()

# Example usage:
# radiobutton_locator = (By.ID, 'radiobutton_id')
# radiobutton_handler = RadioButtonHandler(driver)
# radiobutton_handler.select_radio_button(radiobutton_locator)
