from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that



class TestLoginUI:
    def test_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_title = driver.title
        assert driver.title == "OrangeHRM"

    def test_header(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/")

        title = driver.find_element(By.XPATH,"//h5[normalize-space()='Login']").text
        assert_that("Login").is_equal_to(title)
