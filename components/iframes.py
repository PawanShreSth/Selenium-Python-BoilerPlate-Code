class IframeHandler:
    def __init__(self, driver):
        self.driver = driver

    
    def switch_to_iframe(self, iframe_locator: str):
        iframe = self.driver.find_element(iframe_locator)
        self.driver.switch_to.frame(iframe)

    
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()