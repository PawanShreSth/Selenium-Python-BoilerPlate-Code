from selenium.webdriver.support.ui import WebDriverWait

from variables_for_component import get_explicit_wait_time

from utils.utils import wait_for_presence_of_element



class ButtonHandler:
    def __init__(self, driver):
        self.driver = driver
        self.explicit_wait_time = get_explicit_wait_time()
    
    def click_button(self, locator):
        # Assuming that the tuple or list looks like: (By.ID, 'button_id')
        self.driver.find_element(*locator).click()

    
    def click_button_with_wait(self, locator):
        wait_time = get_explicit_wait_time()

        # Assuming that the tuple or list looks like: (By.ID, 'button_id')
        locator_strategy = locator[0]
        locator_value = locator[1]

        # Wait for an element with ID 'some-id' with a maximum timeout of 10 seconds or seconds as specified in the environment variables
        button_element = wait_for_presence_of_element(self.driver, locator_strategy, locator_value, wait_time)

        if(not button_element):
            button_element.click()
        else:
            print("Failed to click on the Button")


# Example usage:
# button_locator = (By.ID, 'button_id')
# button_handler = ButtonHandler(driver)
# button_handler.click_button(button_locator)

