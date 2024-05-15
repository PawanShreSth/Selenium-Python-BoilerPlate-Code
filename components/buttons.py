class ButtonHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def click_button(self, locator):
        self.driver.find_element(locator).click()

# Example usage:
# button_locator = (By.ID, 'button_id')
# button_handler = ButtonHandler(driver)
# button_handler.click_button(button_locator)
