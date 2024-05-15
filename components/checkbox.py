class CheckboxHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def select_checkbox(self, locator):
        checkbox = self.driver.find_element(*locator)
        if not checkbox.is_selected():
            checkbox.click()

# Example usage:
# checkbox_locator = (By.ID, 'checkbox_id')
# checkbox_handler = CheckboxHandler(driver)
# checkbox_handler.select_checkbox(checkbox_locator)
