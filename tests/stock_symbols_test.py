import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.google_finance import GoogleFinancePage

GIVEN_TEST_DATA = ["NFLX", "MSFT", "TSLA"]


@pytest.fixture(scope="session")
def driver():
    print("\nSetting up the WebDriver\n")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    print("\nTearing down the WebDriver\n")
    driver.quit()


@pytest.fixture(scope="session")
def google_finance_page(driver):
    page = GoogleFinancePage(driver)
    return page


def test_open_google_finance(google_finance_page):
    # google_finance_page.open()
    assert google_finance_page.verify_page_title(), "\nPage title does not match.\n"


def test_retrieve_stock_symbols(google_finance_page):
    listed_symbols = google_finance_page.get_stock_symbols()
    assert len(listed_symbols) > 0, "\nNo stock symbols found on the page.\n"
    return listed_symbols


def get_not_in_given_data_symbols(google_finance_page):
    listed_symbols = test_retrieve_stock_symbols(google_finance_page)
    return [symbol for symbol in listed_symbols if symbol not in GIVEN_TEST_DATA]


def get_not_listed_symbols(google_finance_page):
    listed_symbols = test_retrieve_stock_symbols(google_finance_page)
    return [symbol for symbol in GIVEN_TEST_DATA if symbol not in listed_symbols]


def test_compare_stock_symbols(google_finance_page):
    not_in_given_data = get_not_in_given_data_symbols(google_finance_page)
    not_listed = get_not_listed_symbols(google_finance_page)
    print(f"\nSymbols listed, but not in given test data: {not_in_given_data}\n")
    print(f"\nSymbols in given test data, but not listed: {not_listed}\n")
    assert len(not_in_given_data) > 0 or len(not_listed) > 0, "\nNo difference found between UI and test data.\n"


def test_print_not_in_given_data_symbols(google_finance_page):
    not_in_given_data = get_not_in_given_data_symbols(google_finance_page)
    print(f"\nSymbols listed, but not in given test data: {not_in_given_data}\n")
    assert len(not_in_given_data) > 0, "\nSymbols listed, but not in given test data not found\n"


def test_print_not_listed_symbols(google_finance_page):
    not_listed = get_not_listed_symbols(google_finance_page)
    print(f"\nSymbols in given test data, but not listed: {not_listed}\n")
    assert len(not_listed) > 0, "\nSymbols in given test data, but not listed not found\n"
