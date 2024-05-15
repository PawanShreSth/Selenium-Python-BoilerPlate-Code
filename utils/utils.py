import json
import os
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def read_json(file_path: str) -> dict:
    """
        This function parses JSON data retrieved from the designated file path and returns the resulting dictionary. 
        To guarantee cross-compatibility across various operating systems, 
        make use of os.path.join() before passing the file path when this method is called. 
    """

    with open(file_path, 'r') as file:
        return json.load(file)


def get_image_path(image_name: str) -> str:
    """
        Returns the file or image path which is saved within the images directory inside data folder.
    """

    image_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'images', image_name)
    return image_path


def load_environment_variables():
    """
        Load environment variables from .env file

        For access the saved variables, import os package, call this method and user os.getenv("VARIABLE_NAME")
    """

    environment_file_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(environment_file_path)


def wait_for_presence_of_element(driver, locator_strategy: str, locator_value: str, timeout=10):
    
    try:
        # Set up an explicit wait with the specified timeout
        wait = WebDriverWait(driver, timeout)

        # Wait until the element is located
        element = wait.until(EC.presence_of_element_located((locator_strategy, locator_value)))

        return element
    
    except Exception as e:
        print(f"Error occurred while waiting for element: {e}")
        return None