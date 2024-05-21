import os

from pages.LoginPage import Login
from utils.utils import load_environment_variables

load_environment_variables()

def test_login(driver):
    # Example of accessing password from environment variable file
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    
    login = Login(driver)

    login.visit_page(base_url)
    login.enter_username()
    login.enter_password(password)
    login.click_submit()

