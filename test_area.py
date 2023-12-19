import pytest
from selenium import webdriver

from login_page import *

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_form_submission(browser):
    test_value = form_submission(browser, 'John', 'Doe', 'johndoe@gmail.com', '+447519197543', 'Password123')
    if (test_value.text == "Thank's for signing up..!"):
        assert True

def test_form_submisson_batch(browser):
    for x in range(1, 10):
        test_value = form_submission(browser, 'John', 'Doe', 'johndoe@gmail.com', '+447519197543', 'Password123')
        if (test_value.text == "Thank's for signing up..!"):
            assert True
        
def test_form_submission_max(browser):
    for x in range(1, 100):
        test_value = form_submission(browser, 'John', 'Doe', 'johndoe@gmail.com', '+447519197543', 'Password123')
        if (test_value.text == "Thank's for signing up..!"):
            assert True  

def test_fail(browser):
    test_value = form_submission(browser, '', '', '', '', '')
    if (test_value.text == "*This field is Required"):
        assert True
