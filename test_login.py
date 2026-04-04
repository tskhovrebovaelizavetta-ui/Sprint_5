from locators import HeaderLocators, LoginPopupLocators
from helpers import wait_and_click, wait_and_send_keys, wait_for_element


class TestLogin:

    def test_successful_login(self, driver):
        wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)

        wait_and_send_keys(driver, LoginPopupLocators.EMAIL_INPUT, "lizzza888@yandex.ru")
        wait_and_send_keys(driver, LoginPopupLocators.PASSWORD_INPUT, "123")
        wait_and_click(driver, LoginPopupLocators.BUTTON_LOGIN)

        avatar = wait_for_element(driver, HeaderLocators.USER_AVATAR)
        user_name = wait_for_element(driver, HeaderLocators.USER_NAME)

        assert avatar.is_displayed()
        assert "User" in user_name.text
