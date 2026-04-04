from locators import HeaderLocators
from helpers import login_user, wait_and_click, wait_for_element, wait_for_invisibility


class TestLogout:

    def test_successful_logout(self, driver):
        login_user(driver, "lizzza888@yandex.ru", "123")

        wait_and_click(driver, HeaderLocators.BUTTON_LOGOUT)

        wait_for_invisibility(driver, HeaderLocators.USER_AVATAR)
        login_button = wait_for_element(driver, HeaderLocators.BUTTON_LOGIN_REG)

        assert login_button.is_displayed()
