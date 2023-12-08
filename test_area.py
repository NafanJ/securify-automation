import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from main import *

@pytest.fixture
def browser():
    # Initialize the WebDriver (Chrome here) with appropriate options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Add other options as needed
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(10)
    yield driver
    # Teardown - close the browser window after the test
    driver.quit()


def test_form_submission(browser):
    test_value = form_submission(browser)
    if (test_value.text == "Thank's for signing up..!"):
        assert True
        

