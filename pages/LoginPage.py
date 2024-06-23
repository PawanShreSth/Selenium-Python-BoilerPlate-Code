import os
import time
import pytest

from components.element import ElementHandler
from utils.LocatorStrategy import LocatoryStrategySupplier
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.element = ElementHandler(self.driver)
        self.locator_strategy = LocatoryStrategySupplier()

        # Locators
        self.email_field_locator_value ='input[name="username"]'
        self.password_field_locator_value = 'input[name="password"]'
        self.button_locator_value = "//button[contains(text(), 'Submit')]"
        self.logged_in_msg_locator_value = "h1[class='post-title']"
        self.button_locator_value_2 = "button[type='submit']"


    def visit_page(self, base_url: str):
        self.driver.maximize_window()
        self.driver.get(base_url) 
        main_page_title = "Test Login | Practice Test Automation"

        assert main_page_title == self.driver.title

    
    # Fo login_test.py
    def enter_username(self):
        locator_strategy_value = (By.CSS_SELECTOR, self.email_field_locator_value)

        # Passing use_wait and wait_time is optional
        # if use_wait is not passed by default it is False meaning no wait will be applied.
        # self.element.get_element(locator_strategy_value, True, 5) Here the element is explicitly waitied and 5 second wait time is applied

        email_field = self.element.get_element(locator_strategy_value)
        email_field.send_keys("student")


    def enter_password(self, password: str):
        locator_strategy_value = (By.CSS_SELECTOR, self.password_field_locator_value)

        password_field = self.element.get_element(locator_strategy_value)
        password_field.send_keys(password)


    def click_submit(self):
        locator_strategy_value = (By.XPATH, self.button_locator_value)

        # Using explicit wait
        button = self.element.get_element(locator_strategy_value, use_wait=True, wait_time=5)
        button.click()

    
    def checkLoggedInMessage(self):
        locator_strategy_value = (By.CSS_SELECTOR, self.logged_in_msg_locator_value)

        heading_element = self.element.get_element(locator_strategy_value, wait_time=True)

        is_visible = heading_element.is_displayed()

        assert is_visible
        assert "Logged In" == heading_element.text

    
    # Fo login2_test.py
    def enter_username_2(self):
        locator_strategy_value = (By.CSS_SELECTOR, self.email_field_locator_value)

        email_field = self.element.get_element(locator_strategy_value, use_wait=True)
        email_field.send_keys("practice")


    def enter_password_2(self):
        locator_strategy_value = (By.CSS_SELECTOR, self.password_field_locator_value)


        password_field = self.element.get_element(locator_strategy_value)
        password_field.send_keys("SuperSecretPassword!")

    
    def click_submit_2(self):
        locator_strategy_value = (By.CSS_SELECTOR, self.button_locator_value_2)

        button = self.element.get_element(locator_strategy_value)
        button.click()


    