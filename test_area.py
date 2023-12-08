import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from main import *

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager(version="119.0.6045.199").install())
    # Initialize the WebDriver (Chrome here) with appropriate options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Add other options as needed
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    yield driver
    # Teardown - close the browser window after the test
    driver.quit()


def test_form_submission(browser):
    test_value = form_submission(browser)
    if (test_value.text == "Thank's for signing up..!"):
        assert True
        

