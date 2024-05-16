from utils.utils import wait_for_presence_of_element, get_explicit_wait_time



class ElementHandler:
    def __init__(self, driver):
        self.driver = driver
        
    
    def get_element(self, locator: tuple, use_wait: bool, wait_time=10):
        """
            if use_wait is true is specified, the element will be retrieved by applying explicit wait.
            Otherwise, no wait will be applied.
        """

        # Assuming that the tuple (locator) looks like: (By.ID, 'button_id')
        if (use_wait == True):
            element = self.get_element_explicitly(locator, wait_time)
            return element
        
        element = self.driver.find_element(*locator)

        return element

    
    def get_element_explicitly(self, locator: tuple, wait_time: int):
        locator_strategy = locator[0]
        locator_value = locator[1]

        element = wait_for_presence_of_element(self.driver, locator_strategy, locator_value, wait_time)

        return element



# Example usage:
# button_locator = (By.ID, 'button_id')
# button_handler = ButtonHandler(driver)
# button_handler.click_button(button_locator)
