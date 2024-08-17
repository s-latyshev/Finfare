from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleFinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/finance"
        self.wait = WebDriverWait(self.driver, 5)
        self.open()

    def open(self):
        self.driver.get(self.url)

    def verify_page_title(self):
        return "Google Finance" in self.driver.title

    def get_stock_symbols(self):
        section = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fAThCb")),
            "Section is not found"
        )
        symbols = section.find_elements(By.CSS_SELECTOR, ".COaKTb")
        return [symbol.text for symbol in symbols]

    def close(self):
        self.driver.quit()
