from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.oracle.com/in/database/")
print(driver)
driver.find_element(By.ID, 'acctBtnLabel').click()
driver.find_element(By.XPATH, '//a[normalize-space()="Sign-In"]').click()
# abc = driver.find_element(By.XPATH,"//h2[normalize-space()='Oracle account sign in']")
# driver.switch_to.active_element(abc)
time.sleep(2)

print("test1")
driver.find_element(By.ID, 'sso_username').send_keys("Maulin")
driver.find_element(By.ID, 'ssopassword').send_keys("desai")
driver.find_element(By.ID, 'signin_button').click()
error = driver.find_element(By.XPATH, '//span[@id="errormsg"]//div[1]')
# assert error == "Invalid username and/or password."
# print(error, 'pass')
time.sleep(1)
driver.quit()
