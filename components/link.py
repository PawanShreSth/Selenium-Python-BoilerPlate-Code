class LinkHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def click_link(self, locator):
        self.driver.find_element(*locator).click()

# Example usage:
# link_locator = (By.ID, 'link_id')
# link_handler = LinkHandler(driver)
# link_handler.click_link(link_locator)
