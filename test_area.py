import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from main import *

@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield driver
    # Teardown - close the browser window after the test
    driver.quit()


def test_form_submission(browser):
    test_value = form_submission(browser)
    if (test_value.text == "Thank's for signing up..!"):
        assert True
        

