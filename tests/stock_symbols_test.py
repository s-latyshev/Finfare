import pytest
from page_objects.google_finance_page import GoogleFinancePage

GIVEN_TEST_DATA = ["NFLX", "MSFT", "TSLA"]


@pytest.fixture(scope="session")
def google_finance_page(browser, base_url):
    page = GoogleFinancePage(browser, base_url)
    return page


def test_open_google_finance(google_finance_page):
    assert "Google Finance" in google_finance_page.get_page_title, "\nPage title does not match.\n"


def test_retrieve_stock_symbols(google_finance_page):
    listed_symbols = google_finance_page.get_stock_symbol_texts
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
