from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, LoginPopupLocators, RegisterPopupLocators
from helpers import generate_email, wait_and_click, wait_and_send_keys
from data import EMAIL, PASSWORD, INVALID_EMAIL, REG_PASSWORD


class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()

        wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)
        wait_and_click(driver, LoginPopupLocators.BUTTON_NO_ACCOUNT)

        wait_and_send_keys(driver, RegisterPopupLocators.EMAIL_INPUT, email)
        wait_and_send_keys(driver, RegisterPopupLocators.PASSWORD_INPUT, REG_PASSWORD)
        wait_and_send_keys(driver, RegisterPopupLocators.PASSWORD_CONFIRM_INPUT, REG_PASSWORD)
        wait_and_click(driver, RegisterPopupLocators.BUTTON_CREATE_ACCOUNT)

        # Элемент-маркер успеха только в ассерте (замечание 4)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HeaderLocators.USER_AVATAR)
        ).is_displayed()

    def test_registration_with_invalid_email(self, driver):
        wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)
        wait_and_click(driver, LoginPopupLocators.BUTTON_NO_ACCOUNT)

        wait_and_send_keys(driver, RegisterPopupLocators.EMAIL_INPUT, INVALID_EMAIL)
        wait_and_click(driver, RegisterPopupLocators.BUTTON_CREATE_ACCOUNT)

        # Проверяем наличие элемента ошибки, а не текст (замечание 6)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPopupLocators.ERROR_MESSAGE)
        ).is_displayed()

    def test_registration_existing_user(self, driver):
        wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)
        wait_and_click(driver, LoginPopupLocators.BUTTON_NO_ACCOUNT)

        wait_and_send_keys(driver, RegisterPopupLocators.EMAIL_INPUT, EMAIL)
        wait_and_send_keys(driver, RegisterPopupLocators.PASSWORD_INPUT, PASSWORD)
        wait_and_send_keys(driver, RegisterPopupLocators.PASSWORD_CONFIRM_INPUT, PASSWORD)
        wait_and_click(driver, RegisterPopupLocators.BUTTON_CREATE_ACCOUNT)

        # Проверяем наличие элемента ошибки, а не текст (замечание 6)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPopupLocators.ERROR_MESSAGE)
        ).is_displayed()
