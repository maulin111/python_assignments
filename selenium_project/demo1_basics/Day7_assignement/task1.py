import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
url = "https://github.com/login"
driver.get(url)
driver.find_element(By.ID,"login_field").send_keys("Maulin.desai@einfochips.com")
driver.find_element(By.ID,"password").send_keys("maulin@desai11")
driver.find_element(By.XPATH,"//input[@name='commit']").click()
time.sleep(1)