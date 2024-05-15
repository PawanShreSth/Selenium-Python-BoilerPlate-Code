class TextAreaHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def enter_text_in_textarea(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

# Example usage:
# textarea_locator = (By.ID, 'textarea_id')
# textarea_handler = TextAreaHandler(driver)
# textarea_handler.enter_text_in_textarea(textarea_locator, 'Sample text')
