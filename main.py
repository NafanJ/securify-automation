from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def form_submission(driver):
    driver.get("https://nafanj.github.io/securify/")
    elem = driver.find_element(By.ID, "f-name")
    elem.clear()
    elem.send_keys("John")

    elem = driver.find_element(By.ID, "l-name")
    elem.clear()
    elem.send_keys("Doe")

    elem = driver.find_element(By.ID, "mail")
    elem.clear()
    elem.send_keys("test@gmail.com")

    elem = driver.find_element(By.ID, "phone")
    elem.clear()
    elem.send_keys("07519197543")

    elem = driver.find_element(By.ID, "user-password")
    elem.clear()
    elem.send_keys("Password123")

    elem = driver.find_element(By.ID, "user-password-confirm")
    elem.clear()
    elem.send_keys("Password123")


    elem = driver.find_element(By.XPATH, '//*[@id="btm"]/button')
    elem.click()

    elem = driver.find_element(By.XPATH, '/html/body/section/h1[2]')
    return elem