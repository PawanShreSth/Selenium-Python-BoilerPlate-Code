import os
import sys

# Add the directory to sys.path.
# The path may vary based on which OS is used or where the file is located.
# Done to precent ModuleNotFoundError
sys.path.append("C:\Selenium Boiler Plate")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.LoginPage import Login
from utils.utils import load_environment_variables

load_environment_variables()

# Setting up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode


# Using WebDriver Manager to automatically handle the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def login():
    # Example of accessing password from environment variable file
    password = os.getenv("PASSWORD")
    login = Login(driver)

    login.visit_page()
    login.enter_username()
    login.enter_password(password)
    login.click_submit()


login()