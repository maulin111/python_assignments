import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.online.citibank.co.in/")

driver.find_element(By.XPATH,"//a[@title='Close']").click()
driver.find_element(By.XPATH,"//span[@class='lockSign']").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH,"//div[contains(text(),'Forgot User ID?')]").click()
driver.find_element(By.LINK_TEXT,"Credit Card']").click()
driver.find_element(By.ID,"citiCard1").send_keys(7897)
driver.find_element(By.ID,"citiCard2").send_keys(7897)
driver.find_element(By.ID,"citiCard3").send_keys(7897)
driver.find_element(By.ID,"citiCard4").send_keys(7897)

driver.find_element(By.NAME,"CCVNO").send_keys(345)

driver.find_element(By.ID,"bill-date-long").click()

select_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
select_year.select_by_visible_text("2000")

select_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
select_month.select_by_visible_text("Apr")

