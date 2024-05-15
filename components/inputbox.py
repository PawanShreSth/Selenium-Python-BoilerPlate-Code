class EditBoxHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def enter_text_in_editbox(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

# Example usage:
# editbox_locator = (By.ID, 'editbox_id')
# editbox_handler = EditBoxHandler(driver)
# editbox_handler.enter_text_in_editbox(editbox_locator, 'Sample text')
