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

def test_empty_fname(browser):
    test_value = form_submission(browser, '', 'Doe', 'johndoe@gmail.com', '+447519197543', 'Password123')
    if (test_value.text == "*This field is Required"):
        assert True

def test_empty_lname(browser):
    test_value = form_submission(browser, 'John', '', 'johndoe@gmail.com', '+447519197543', 'Password123')
    if (test_value.text == "*This field is Required"):
        assert True

def test_empty_mail(browser):
    test_value = form_submission(browser, 'John', 'Doe', '', '+447519197543', 'Password123')
    if (test_value.text == "*This field is Required"):
        assert True

def test_empty_phone(browser):
    test_value = form_submission(browser, 'John', 'Doe', 'johndoe@gmail.com', '', 'Password123')
    if (test_value.text == "*This field is Required"):
        assert True

def test_empty_password(browser):
    test_value = form_submission(browser, 'John', 'Doe', 'johndoe@gmail.com', '+447519197543', '')
    if (test_value.text == "*This field is Required"):
        assert True

def test_fail(browser):
    test_value = form_submission(browser, '', 'Doe', 'johndoe@gmail.com', '+447519197543', 'Password123')
    if (test_value.text == "*This field is Required"):
        assert False