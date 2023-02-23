# importing webdriver from selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

url = "https://www.facebook.com/"

driver.get(url)

driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("John")
driver.find_element(By.NAME,"lastname").send_keys("Doe")
driver.find_element(By.ID,"password_step_input").send_keys("Test@123")
driver.find_element(By.XPATH,'(//input[@type="radio"])[2]').click()
driver.find_element(By.NAME,'websubmit').click()
time.sleep(2)



