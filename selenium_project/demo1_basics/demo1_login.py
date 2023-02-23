# importing webdriver from selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.facebook.com/"

driver.get(url)
get_title = driver.title
print(get_title)
# ele = driver.find_element(By.ID,"email")
# ele.send_keys("maulin.desai@gmail.com")
driver.find_element(By.ID,"email").send_keys("maulin.desai@gmail.com")
driver.find_element(By.ID,"pass").send_keys("Test@123")
time.sleep(5)
driver.find_element(By.NAME,"login").click()
x = driver.find_element(By.XPATH,"//div[@id='header_block']//span//div").text
assert x == "Log in to Facebook"
print(x," - pass")
driver.quit()
