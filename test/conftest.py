import pytest
import sys
import os

# To remove ModuleNotFoundError
sys.path.append("C:\\Selenium Boiler Plate")

from utils.utils import load_environment_variables
from utils.driver_factory import DriverFactory

load_environment_variables()


@pytest.fixture(scope='session')
def driver():
    browser = os.getenv("BROWSER", "chrome")  # Default to Chrome if BROWSER is not set
    driver = DriverFactory.get_driver(browser)
    yield driver
    print("Close application")
    driver.quit()


# Example usage (name of the fixture and the method's parameter should be same)
# def test_login(driver):
#    ...