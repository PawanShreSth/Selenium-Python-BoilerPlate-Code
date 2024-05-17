import os
import time

from components.element import ElementHandler
from utils.LocatorStrategy import LocatoryStrategySupplier
from selenium.webdriver.common.by import By

from .LoginPageLocator import LoginPageLocatorSupplier

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.element = ElementHandler(self.driver)
        self.locator_strategy = LocatoryStrategySupplier()

        #Locators Value
        self.locators = LoginPageLocatorSupplier()

    def visit_page(self, base_url: str):
        self.driver.maximize_window()
        self.driver.get(base_url) 

    
    def enter_username(self):
        locator_strategy = self.locator_strategy.locate_element_by("CSS") # returns By.CSS_SELECTOR
        locator_strategy_value = (locator_strategy, self.locators.email_field_locator_value)

        # Passing use_wait and wait_time is optional
        # if use_wait is not passed by default it is False meaning no wait will be applied.
        # self.element.get_element(locator_strategy_value, True, 5) Here the element is explicitly waitied and 5 second wait time is applied

        email_field = self.element.get_element(locator_strategy_value)
        email_field.send_keys("student")


    def enter_password(self, password: str):
        locator_strategy = self.locator_strategy.locate_element_by("CSS") # returns By.CSS_SELECTOR
        locator_strategy_value = (locator_strategy, self.locators.password_field_locator_value)


        password_field = self.element.get_element(locator_strategy_value)
        password_field.send_keys(password)

    
    def click_submit(self):
        locator_strategy = self.locator_strategy.locate_element_by("XPATH") # returns By.CSS_SELECTOR
        locator_strategy_value = (locator_strategy, self.locators.button_locator_value)

        # Using explicit wait
        button = self.element.get_element(locator_strategy_value, use_wait=True, wait_time=5)
        button.click()
        time.sleep(10)

