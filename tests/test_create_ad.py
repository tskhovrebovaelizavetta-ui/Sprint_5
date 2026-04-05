from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    HeaderLocators,
    ModalLocators,
    CreateAdLocators,
    DropdownOptionLocators,
    ProfileLocators
)
from helpers import login_user, wait_and_click, wait_and_send_keys
from data import EMAIL, PASSWORD, AD_NAME, AD_DESCRIPTION, AD_PRICE, AD_CATEGORY, AD_CITY


class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        wait_and_click(driver, HeaderLocators.BUTTON_PLACE_AD)

        # Текст перенесён в селектор, проверяем наличие элемента через is_displayed (замечание 3)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ModalLocators.MODAL_TITLE_AUTH_REQUIRED)
        ).is_displayed()

    def test_create_ad_authorized(self, driver):
        login_user(driver, EMAIL, PASSWORD)

        wait_and_click(driver, HeaderLocators.BUTTON_PLACE_AD)

        wait_and_send_keys(driver, CreateAdLocators.NAME_INPUT, AD_NAME)
        wait_and_send_keys(driver, CreateAdLocators.DESCRIPTION_INPUT, AD_DESCRIPTION)
        wait_and_send_keys(driver, CreateAdLocators.PRICE_INPUT, AD_PRICE)

        wait_and_click(driver, CreateAdLocators.CATEGORY_ARROW)
        wait_and_click(driver, DropdownOptionLocators.category_option(AD_CATEGORY))

        wait_and_click(driver, CreateAdLocators.CITY_ARROW)
        wait_and_click(driver, DropdownOptionLocators.city_option(AD_CITY))

        wait_and_click(driver, CreateAdLocators.RADIO_NEW)

        current_url = driver.current_url
        wait_and_click(driver, CreateAdLocators.BUTTON_PUBLISH)

        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        wait_and_click(driver, ProfileLocators.PROFILE_LINK)

        # Проверка наличия карточки объявления только в ассерте (замечание 3)
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfileLocators.AD_CARD)
        ).is_displayed()
