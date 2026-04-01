import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from helpers import login_user, EXISTING_EMAIL, EXISTING_PASSWORD, open_login_form
from locators.header import HeaderLocators
from base_page import BasePage
from helpers import login_user, register_user, generate_email

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

class TestLogout:
    def test_logout_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        base_page = BasePage(driver)
        
        # Авторизация
        login_user(driver)
        
        # Проверка что пользователь авторизован
        base_page.wait_visible(HeaderLocators.USER_NAME)
        
        # Выход
        base_page.wait_click(HeaderLocators.LOGOUT_BUTTON)
        
        # Проверка исчезновения аватара и появления кнопки входа
        base_page.wait_visible(HeaderLocators.LOGIN_BUTTON)
        # Проверяем что имя пользователя исчезло
        assert not base_page.driver.find_elements(*HeaderLocators.USER_NAME)