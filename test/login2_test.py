import os

from pages.LoginPage import Login
from utils.utils import load_environment_variables
load_environment_variables()

def test_login(driver):
    # Example of accessing password from environment variable file
    base_url = os.getenv("OTHER_URL")
    
    login = Login(driver)

    login.visit_page(base_url)
    login.enter_username_2()
    login.enter_password_2()
    login.click_submit_2()
    