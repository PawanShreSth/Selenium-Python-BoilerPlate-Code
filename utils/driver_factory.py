from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == 'chrome':
            # Setting up Chrome options (optional)
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        driver.maximize_window()
        return driver
