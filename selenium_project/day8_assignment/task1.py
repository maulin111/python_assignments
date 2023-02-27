from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.oracle.com/in/database/")
print(driver.session_id)
driver.find_element(By.ID, 'acctBtnLabel').click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Sign-In").click()

print(driver.title)
print(driver.current_url)

header=driver.find_element(By.XPATH,"//h2").text
print(header)

driver.find_element(By.ID, 'sso_username').send_keys("Maulin")
driver.find_element(By.ID, 'ssopassword').send_keys("desai")
driver.find_element(By.ID, 'signin_button').click()
time.sleep(3)
error = driver.find_element(By.XPATH,"//div[contains(text(),'Invalid')]").text
assert error == "Invalid username and/or password."

print(error, 'pass')

