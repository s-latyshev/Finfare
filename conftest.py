import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    print("\nSetting up the WebDriver\n")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    print("\nTearing down the WebDriver\n")
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://www.google.com/"
