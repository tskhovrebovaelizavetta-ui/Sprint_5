import pytest
from selenium import webdriver
from base_page import BasePage
from locators.header import HeaderLocators
from helpers import login_user
from locators.header import HeaderLocators
from helpers import login_user, register_user, generate_email

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        self.page = BasePage(self.driver)
    
    def teardown(self):
        self.driver.quit()
    
    def test_login_user(self):
        login_user(self.driver)
        user_name = self.page.wait_visible(HeaderLocators.USER_NAME)
        assert "User" in user_name.text