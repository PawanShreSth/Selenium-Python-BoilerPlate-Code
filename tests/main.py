from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginTest import login

import time

from selenium.webdriver.common.by import By

# Setting up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode


# Using WebDriver Manager to automatically handle the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Example usage: Opening a webpage
login(driver)