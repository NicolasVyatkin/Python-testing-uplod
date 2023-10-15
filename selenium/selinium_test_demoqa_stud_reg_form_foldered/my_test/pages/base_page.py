from selenium.webdriver.support.ui import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """class that contains basic functions"""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """function that opens page"""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """function that finds visible element on the page"""
        return WDWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """function that finds all visible elements on the page"""
        return WDWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def remove_footer(self):
        """function that removes some html/css element from the page"""
        self.driver.execute_script(
            "document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script(
            'document.getElementById("fixedban").style.display="none"')
