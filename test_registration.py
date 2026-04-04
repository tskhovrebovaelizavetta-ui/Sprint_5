from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, LoginPopupLocators, RegisterPopupLocators
from helpers import generate_email, wait_and_click, wait_and_send_keys, wait_for_element


class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()
        password = "password123"

        wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)
        wait_and_click(driver, LoginPopupLocators.BUTTON_NO_ACCOUNT)

        wait_and_send_keys(driver, RegisterPopupLocators.EMAIL_INPUT, email)
        wait_and_send_keys(driver, RegisterPopupLocators.PASSWORD_INPUT, password)
        wait_and_send_keys(driver, RegisterPopupLocators.PASSWORD_CONFIRM_INPUT, password)
        wait_and_click(driver, RegisterPopupLocators.BUTTON_CREATE_ACCOUNT)

        avatar = wait_for_element(driver, HeaderLocators.USER_AVATAR)
        user_name = wait_for_element(driver, HeaderLocators.USER_NAME)

        assert avatar.is_displayed()
        assert "User" in user_name.text

    def test_registration_with_invalid_email(self, driver):
        wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)
        wait_and_click(driver, LoginPopupLocators.BUTTON_NO_ACCOUNT)

        wait_and_send_keys(driver, RegisterPopupLocators.EMAIL_INPUT, "invalid_email")
        wait_and_click(driver, RegisterPopupLocators.BUTTON_CREATE_ACCOUNT)

        error_message = wait_for_element(driver, RegisterPopupLocators.ERROR_MESSAGE)

        assert error_message.text == "Ошибка"

    def test_registration_existing_user(self, driver):
        wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)
        wait_and_click(driver, LoginPopupLocators.BUTTON_NO_ACCOUNT)

        wait_and_send_keys(driver, RegisterPopupLocators.EMAIL_INPUT, "lizzza888@yandex.ru")
        wait_and_send_keys(driver, RegisterPopupLocators.PASSWORD_INPUT, "123")
        wait_and_send_keys(driver, RegisterPopupLocators.PASSWORD_CONFIRM_INPUT, "123")
        wait_and_click(driver, RegisterPopupLocators.BUTTON_CREATE_ACCOUNT)

        error_message = wait_for_element(driver, RegisterPopupLocators.ERROR_MESSAGE)

        assert error_message.text == "Ошибка"
