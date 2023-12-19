from selenium.webdriver.common.by import By

def form_submission(driver, fname, lname, mail, phone, password):
    driver.get("https://nafanj.github.io/securify/")
    elem = driver.find_element(By.ID, "f-name")
    elem.send_keys(fname)

    elem = driver.find_element(By.ID, "l-name")
    elem.send_keys(lname)

    elem = driver.find_element(By.ID, "mail")
    elem.send_keys(mail)

    elem = driver.find_element(By.ID, "phone")
    elem.send_keys(phone)

    elem = driver.find_element(By.ID, "user-password")
    elem.send_keys(password)

    elem = driver.find_element(By.ID, "user-password-confirm")
    elem.send_keys(password)


    elem = driver.find_element(By.XPATH, '//*[@id="btm"]/button')
    elem.click()

    elem = driver.find_element(By.XPATH, '/html/body/section/h1[2]')
    return elem

def form_fail(driver):
    driver.get("https://nafanj.github.io/securify/")

    elem = driver.find_element(By.XPATH, '//*[@id="btm"]/button')
    elem.click()

    elem = driver.find_element(By.XPATH,'/html/body/main/form/div/div[1]/div')
    return elem