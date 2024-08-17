# Stock Symbols Test Automation

## Setup

**Install dependencies:**
use the following command:
pip install -r requirements.txt
or
pip3 install -r requirements.txt

**Install Google Chrome and ChromeDriver**

## Running Tests

To run the tests, use the following command:
pytest -v -s

## GitHub Actions Workflows
The project includes GitHub Actions workflows for running tests manually and on a nightly basis:

Manual Tests Workflow: Allows you to run all tests or specific test cases manually from the GitHub Actions UI.
Available options:
1. full - runs all test cases (default)
2. print_not_in_given_data_symbols
3. print_not_listed_symbols

Nightly Tests Workflow: Automatically runs all tests every night.