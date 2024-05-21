import os
import sys

# Add the directory to sys.path.
# The path may vary based on which OS is used or where the file is located.
# Done to remove ModuleNotFoundError by adding the folder path to the system path
sys.path.append("C:\Selenium Boiler Plate")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.driver_factory import DriverFactory
from pages.LoginPage import Login
from utils.utils import load_environment_variables

load_environment_variables()



driver = DriverFactory.get_driver(os.getenv("BROWSER"))

def login():
    # Example of accessing password from environment variable file
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    
    login = Login(driver)

    login.visit_page(base_url)
    login.enter_username()
    login.enter_password(password)
    login.click_submit()


login()