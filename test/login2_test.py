import os

from pages.LoginPage import Login
from utils.utils import load_environment_variables
load_environment_variables()

def test_login(driver):
    # Example of accessing password from environment variable file
    password = "hehehhe"
    base_url = os.getenv("BASE_URL")
    
    login = Login(driver)

    login.visit_page("https://practice.expandtesting.com/login")
    login.enter_username_2()
    login.enter_password_2()
    login.click_submit_2()

# test_login()