import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
url = "https://www.salesforce.com/in/form/signup/freetrial-sales/"
driver.get(url)
driver.find_element(By.NAME, "UserFirstName").send_keys("John")
driver.find_element(By.NAME, "UserLastName").send_keys("wick")
driver.find_element(By.NAME, "UserEmail").send_keys("John@abc.com")
driver.find_element(By.XPATH, "//option[@value='IT_Manager_AP']").click()
driver.find_element(By.NAME, "CompanyName").send_keys("Einfochips")
driver.find_element(By.XPATH, "//option[@value='250']").click()
driver.find_element(By.XPATH, "//option[@value='GB']").click()
driver.find_element(By.XPATH, "//span[@class='error-msg-block']/../div[@class='checkbox-ui']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='start my free trial']").click()
time.sleep(1)
x = driver.find_element(By.XPATH, "//span[.='Enter a valid phone number']").text
assert x == "Enter a valid phone number"
print(x," - pass")
time.sleep(1)
