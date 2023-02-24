from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.db4free.net/")

driver.find_element(By.XPATH, '//b[normalize-space()="phpMyAdmin »"]').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,"input_username").send_keys("maulin")
driver.find_element(By.ID,"input_password").send_keys("desai")
driver.find_element(By.ID,"input_go").click()

print(driver.title)

time.sleep(3)