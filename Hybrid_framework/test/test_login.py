import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_validlogin(self):
        print("valid login")

class TestLoginUI:

    @pytest.fixture(scope="function", autouse=True)
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

    def test_header(self):
        title = self.driver.find_element(By.XPATH, "//h5[normalize-space()='Login']").text
        assert_that("Login").is_equal_to(title)

    def test_validlogin(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        actual_text = self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_text)

