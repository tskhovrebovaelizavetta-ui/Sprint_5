from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators
from helpers import login_user, wait_and_click, wait_for_invisibility
from data import EMAIL, PASSWORD


class TestLogout:

    def test_successful_logout(self, driver):
        login_user(driver, EMAIL, PASSWORD)

        wait_and_click(driver, HeaderLocators.BUTTON_LOGOUT)

        wait_for_invisibility(driver, HeaderLocators.USER_AVATAR)

        # Элемент-маркер успеха только в ассерте (замечание 4)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HeaderLocators.BUTTON_LOGIN_REG)
        ).is_displayed()
