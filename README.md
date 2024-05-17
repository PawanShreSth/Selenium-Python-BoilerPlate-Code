# Selenium Python Project

# Getting Started

- Python 3.11.4: Ensure you have Python 3.11.4 installed on your machine.
- PIP Package Manager: Ensure PIP is installed for managing Python packages.

# Recommended Code Editors

To work with the Selenium boilerplate, it is recommended to use one of the following editors:

- Visual Studio Code (Recommended)
- PyCharm

# Installations

- pip install python-dotenv (https://pypi.org/project/python-dotenv/)
- pip install -U selenium (https://pypi.org/project/selenium/)
- pip install webdriver-manager (https://pypi.org/project/webdriver-manager/)

# Configuration for using the test script

1. Create a .env File: In the root directory of your project, create a .env file and specify the following environment variables:
   Example of where to store `.env` is shown by using the file `.env.example`

   Set the follwing variable to use the boiler plate script.
   `USERNAME=your_username`
   `PASSWORD=your_password`
   `BASE_URL=your_base_url`

3. Change Directory: Navigate to the Selenium Boiler Plate directory. You can do this using the terminal or command prompt:

   `cd path/to/Selenium\ Boiler\ Plate`

4. Run the Test Script: Use the Command Line Interface (CLI) to run the test script. Replace login_test.py with the name of your script if different:

   `python .\test\login_test.py`

# **\*\***\*\***\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***\*\***\*\***\_**\*\***\*\***\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***\*\***\*\***

## Folder Structure Overview

This Selenium Python project adopts a structured approach to facilitate clean, maintainable, and scalable code.
The folder structure is designed to organize components, data, pages, tests, and utilities effectively.

### 1. component folder

- **element.py**: Houses the `ElementHandler` class.

  - **ElementHandler Class**:
    - `get_element`: This method retrieves a web element.
    - If the `use_wait` argument is `True`, it applies an explicit wait before returning the element and by default wait time is 10 but can be changed by using key word argument: `wait_for`=3.
    - Both `use_wait` and `wait_for` are optional.
    - If `use_wait` is `False`, it returns the element without any wait.
    - `wait_for` is not used if the `use_wait` is False, which by default it is.

### 2. data folder

This directory stores various types of test data required for testing.

- **images**: Stores images for use in test scripts.
- **valid_data**: Contains valid data files (e.g., JSON) for testing.
- **invalid_data**: Contains invalid data files (e.g., JSON) for testing.

### 3. pages and tests folder

Following the Page Object Model (POM) design pattern, these folders organize locators and methods for pages and tests, respectively.

- **pages**: Contains page classes representing specific web pages.

  - **LoginPage.py**: Defines the `LoginPage` class, which is used to locate and interact with elements on the login page.

    - **Methods**:
      - `enter_username()`: Enters the provided username into the username field.
      - `enter_password(password)`: Enters the provided password into the password field.
      - `click_submit()`: Clicks on the submit button.

    This class demonstrates how to utilize the Selenium boilerplate in writing
    page level code.

  - **Locator files**: Additional files ending with "Locator" store element locator values used in corresponding page classes.

- **tests**: Stores test scripts that utilize class and methods defined in the `pages` folder.

  - **login_test.py**: Demonstrates usage of `load_environment_variables`. Additionally, includes an import workaround: `sys.path.append("C:\Selenium Boiler Plate")` to address `ModuleNotFoundError`.

### 4. utils folder

This folder houses utility methods for various functionalities across the project.

- **utils.py**: Contains reusable utility methods:

  - `read_json(file_path)`: Reads and parses JSON data from the specified file path and returns the data.
  - `get_path(file_name, path_for)`: Returns the full path of a stored file based on the `file_name` and `path_for` parameters, where `path_for` specifies the data folder subdirectory.
  - `load_environment_variables()`: Loads environment variables from the `.env` file using `os.getenv("VARIABLE_NAME")`.
  - `wait_for_presence_of_element(driver, by, value)`: Defines explicit wait logic used by the `get_element` method in the `ElementHandler` class.

  - **LocatorStrategy.py**: Contains a `LocatorStrategySupplier` class with a `locate_element_by` method. This method returns `By` values based on the `locate_by` argument, providing flexibility in element location strategies.

### 5. .env file

This file defines environment variables for use across the project, loaded using the `load_environment_variable` method.

`.env.example`: This file is just for showing where to store the .env file and how to use it.

### 6. .gitignore file

Specifies files and folders for Git to ignore, ensuring that sensitive or unnecessary files are not tracked in the version control system.
