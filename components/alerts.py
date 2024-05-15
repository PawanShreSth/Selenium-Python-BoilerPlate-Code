from selenium.webdriver.common.alert import Alert

class AlertHandler:
    def __init__(self, driver):
        self.driver = driver

    def focus_on_alert(self):
        """
            Intially the focus is on the main window, to change it use this prior to using other methods defined in AlertHandler.
        """
        self.driver.switch_to.alert()

    
    def accept_alert(self):
        Alert(self.driver).accept()

    
    def dismiss_alert(self):
        Alert(self.driver).dismiss()

    
    def get_alert_text(self):
        return Alert(self.driver).text

    
    def send_keys_to_alert(self, keys: str):
        Alert(self.driver).send_keys(keys)

    
