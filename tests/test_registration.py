import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from helpers import generate_email, open_registration_form, PASSWORD
from locators.registration import RegistrationLocators
from locators.header import HeaderLocators
from base_page import BasePage
from helpers import login_user, register_user, generate_email

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

@pytest.fixture
def base_page(driver):
    page = BasePage(driver)
    page.go_to("https://qa-desk.stand.praktikum-services.ru/")
    return page

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

class TestRegistration:
    def test_successful_registration(self, driver):
        base_page = BasePage(driver)
        from helpers import generate_email, register_user
        email = generate_email()
        register_user(base_page, email)
        user_name = self.page.wait_visible(HeaderLocators.USER_NAME)
        assert "User" in user_name.text

    def test_registration_invalid_email(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        base_page = BasePage(driver)
        
        open_registration_form(driver)
        base_page.wait_visible(RegistrationLocators.EMAIL_INPUT).send_keys("invalid-email")
        base_page.wait_click(RegistrationLocators.CREATE_ACCOUNT_BUTTON)
        
        # Проверка красной подсветки полей и сообщения об ошибке
        email_field = base_page.wait_visible(RegistrationLocators.EMAIL_INPUT)
        password_field = base_page.wait_visible(RegistrationLocators.PASSWORD_INPUT)
        password_repeat_field = base_page.wait_visible(RegistrationLocators.PASSWORD_REPEAT_INPUT)
        
        assert "spanGlobal" in email_field.get_attribute("class")

    def test_registration_existing_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        base_page = BasePage(driver)
        
        open_registration_form(driver)
        base_page.wait_visible(RegistrationLocators.NAME_INPUT).send_keys("Ivan")
        base_page.wait_visible(RegistrationLocators.SURNAME_INPUT).send_keys("Petrov")
        base_page.wait_visible(RegistrationLocators.EMAIL_INPUT).send_keys("test@example.com")
        base_page.wait_visible(RegistrationLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        base_page.wait_visible(RegistrationLocators.PASSWORD_REPEAT_INPUT).send_keys(PASSWORD)
        base_page.wait_click(RegistrationLocators.CREATE_ACCOUNT_BUTTON)
        surname_field = base_page.wait_visible(RegistrationLocators.SURNAME_INPUT)
        if surname_field:
            surname_field.send_keys("Petrov")
        # Проверка ошибки для существующего пользователя
        email_field = base_page.wait_visible(RegistrationLocators.EMAIL_INPUT)
        error_text = base_page.wait_visible((By.XPATH, "//*[contains(text(), 'Ошибка')]"))
        assert "Ошибка" in error_text.text
        