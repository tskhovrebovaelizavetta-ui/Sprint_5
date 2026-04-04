from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    HeaderLocators,
    ModalLocators,
    CreateAdLocators,
    DropdownOptionLocators,
    ProfileLocators
)
from helpers import login_user, wait_and_click, wait_and_send_keys, wait_for_element


class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        wait_and_click(driver, HeaderLocators.BUTTON_PLACE_AD)

        modal_title = wait_for_element(driver, ModalLocators.MODAL_TITLE)

        assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь"

    def test_create_ad_authorized(self, driver):
        login_user(driver, "lizzza888@yandex.ru", "123")

        wait_and_click(driver, HeaderLocators.BUTTON_PLACE_AD)

        wait_and_send_keys(driver, CreateAdLocators.NAME_INPUT, "Тестовое объявление")
        wait_and_send_keys(driver, CreateAdLocators.DESCRIPTION_INPUT, "Описание тестового товара")
        wait_and_send_keys(driver, CreateAdLocators.PRICE_INPUT, "5000")

        wait_and_click(driver, CreateAdLocators.CATEGORY_ARROW)
        wait_and_click(driver, DropdownOptionLocators.category_option("Технологии"))

        wait_and_click(driver, CreateAdLocators.CITY_ARROW)
        wait_and_click(driver, DropdownOptionLocators.city_option("Москва"))

        wait_and_click(driver, CreateAdLocators.RADIO_NEW)

        current_url = driver.current_url
        wait_and_click(driver, CreateAdLocators.BUTTON_PUBLISH)

        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        wait_and_click(driver, ProfileLocators.PROFILE_LINK)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfileLocators.AD_CARD)
        )
        ads = driver.find_elements(*ProfileLocators.AD_CARD)

        assert len(ads) >= 1
