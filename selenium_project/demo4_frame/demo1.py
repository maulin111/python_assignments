import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://netbanking.hdfcbank.com/netbanking/"

driver.get(url)

time.sleep(2)

driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))
driver.find_element(By.XPATH,("//input[@name='fldLoginUserId']")).send_keys("test123")
driver.find_element(By.XPATH,"//a[contains(.,'CONTINUE')]").click()
time.sleep(2)