import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that



class TestLoginUI:

    @pytest.fixture(scope="function")
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

    def test_header(self,setUp):
        title = self.driver.find_element(By.XPATH,"//h5[normalize-space()='Login']").text
        assert_that("Login").is_equal_to(title)

