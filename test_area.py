import pytest
from selenium import webdriver

from main import *

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_form_submission(browser):
    test_value = form_submission(browser)
    if (test_value.text == "Thank's for signing up..!"):
        assert True

def test_form_submisson_batch(browser):
    for x in range(1, 10):
        test_value = form_submission(browser)
        if (test_value.text == "Thank's for signing up..!"):
            assert True
        

