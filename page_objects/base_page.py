from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import base_url


class BasePage:
    def __init__(self, driver, base_url=base_url, path=""):
        self.driver = driver
        self.base_url = base_url
        self.path = path
        self.full_url = f"{self.base_url}{self.path}"
        self.wait = WebDriverWait(driver, 5)

    def open(self) -> None:
        self.driver.get(self.full_url)

    def find(self, locator, parent_element=None) -> WebElement:
        if parent_element:
            return parent_element.find_element(*locator)
        else:
            return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator, parent_element=None) -> list[WebElement]:
        if parent_element:
            return parent_element.find_elements(*locator)
        else:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
