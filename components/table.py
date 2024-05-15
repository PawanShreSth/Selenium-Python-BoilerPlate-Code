from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TableHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def get_table_cell_value(self, table_locator, row_index, col_index):
        table = self.driver.find_element(*table_locator)
        row = table.find_elements(By.TAG_NAME, "tr")[row_index]
        cell = row.find_elements(By.TAG_NAME, "td")[col_index]
        return cell.text

# Example usage:
# table_locator = (By.ID, 'table_id')
# table_handler = TableHandler(driver)
# cell_value = table_handler.get_table_cell_value(table_locator, 1, 1)
