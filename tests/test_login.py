from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, LoginPopupLocators
from helpers import wait_and_click, wait_and_send_keys
from data import EMAIL, PASSWORD


class TestLogin:

    def test_successful_login(self, driver):
        wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)

        wait_and_send_keys(driver, LoginPopupLocators.EMAIL_INPUT, EMAIL)
        wait_and_send_keys(driver, LoginPopupLocators.PASSWORD_INPUT, PASSWORD)
        wait_and_click(driver, LoginPopupLocators.BUTTON_LOGIN)

        # Элемент-маркер успеха только в ассерте (замечание 4)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HeaderLocators.USER_AVATAR)
        ).is_displayed()
