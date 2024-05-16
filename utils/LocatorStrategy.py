from selenium.webdriver.common.by import By

class LocatoryStrategySupplier:
    def locate_element_by(self, locate_by: str = "ID"):
        if (locate_by.upper() == "ID"):
            return By.ID

        if (locate_by == "NAME"):
            return By.NAME

        if (locate_by == "XPATH"):
            return By.XPATH

        if (locate_by == "CSS"):
            return By.CSS_SELECTOR

        if (locate_by == "CLASS_NAME"):
            return By.CLASS_NAME

        if (locate_by == "TAG_NAME"):
            return By.TAG_NAME

        if (locate_by == "LINK_TEXT"):
            return By.LINK_TEXT

        if (locate_by == "PARTIAL_LINK_TEXT"):
            return By.PARTIAL_LINK_TEXT

        