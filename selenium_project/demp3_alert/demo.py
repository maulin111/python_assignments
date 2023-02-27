import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm"

driver.get(url)

time.sleep(2)
driver.find_element(By.XPATH,"//img[@alt='Go']").click()

time.sleep(2)

actual_alert = driver.switch_to.alert.text
print(actual_alert)

driver.switch_to.alert.accept()


time.sleep(2)