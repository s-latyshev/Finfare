from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from page_objects.base_page import BasePage


class GoogleFinancePage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url, "finance")
        self.open()

    @property
    def get_page_title(self) -> str:
        return self.driver.title

    @property
    def get_stock_symbols_section(self) -> WebElement:
        return self.find((By.CSS_SELECTOR, ".fAThCb"))

    @property
    def get_stock_symbol_elements(self) -> list[WebElement]:
        return self.find_all((By.CSS_SELECTOR, ".COaKTb"), self.get_stock_symbols_section)

    @property
    def get_stock_symbol_texts(self) -> list[str]:
        elements = self.get_stock_symbol_elements
        return [element.text for element in elements]

    def close(self) -> None:
        self.driver.quit()
