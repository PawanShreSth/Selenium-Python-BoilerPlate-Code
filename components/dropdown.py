from selenium.webdriver.support.ui import Select

class DropdownHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def select_option_by_value(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value)
    
    def select_option_by_visible_text(self, locator, text):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text)
    
    def select_option_by_index(self, locator, index):
        select = Select(self.driver.find_element(*locator))
        select.select_by_index(index)

# Example usage:
# dropdown_locator = (By.ID, 'dropdown_id')
# dropdown_handler = DropdownHandler(driver)
# dropdown_handler.select_option_by_value(dropdown_locator, 'option_value')
