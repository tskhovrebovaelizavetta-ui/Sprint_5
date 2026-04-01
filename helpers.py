from selenium.webdriver.common.by import By
from base_page import BasePage
from locators.header import HeaderLocators
from locators.registration import RegistrationLocators
import uuid

EXISTING_EMAIL = "test@example.com"
EXISTING_PASSWORD = "password123"
PASSWORD = "password123"

def generate_email():
    return f"user_{uuid.uuid4().hex[:8]}@example.com"

def open_login_form(driver):
    page = BasePage(driver)
    page.wait_click(HeaderLocators.LOGIN_BUTTON)

def open_registration_form(driver):
    page = BasePage(driver)
    open_login_form(driver)
    page.wait_click(RegistrationLocators.NO_ACCOUNT_BUTTON)

def login_user(driver):
    page = BasePage(driver)
    open_login_form(driver)
    page.wait_visible(RegistrationLocators.EMAIL_INPUT).send_keys(EXISTING_EMAIL)
    page.wait_visible(RegistrationLocators.PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
    page.wait_click((By.XPATH, "//button[contains(text(), 'Войти')]"))

def register_user(driver, email):
    page = BasePage(driver)
    open_registration_form(driver)
    # Заполни все поля регистрации
    page.wait_visible(RegistrationLocators.NAME_INPUT).send_keys("User")
    page.wait_visible(RegistrationLocators.SURNAME_INPUT).send_keys("Test")
    page.wait_visible(RegistrationLocators.REG_EMAIL_INPUT).send_keys(email)
    page.wait_visible(RegistrationLocators.REG_PASSWORD_INPUT).send_keys(PASSWORD)
    page.wait_visible(RegistrationLocators.PASSWORD_REPEAT_INPUT).send_keys(PASSWORD)
    page.wait_click(RegistrationLocators.CREATE_ACCOUNT_BUTTON)