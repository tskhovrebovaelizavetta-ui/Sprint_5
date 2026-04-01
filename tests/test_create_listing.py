import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from helpers import login_user, EXISTING_EMAIL, EXISTING_PASSWORD
from locators.header import HeaderLocators
from locators.create_ad import CreateAdLocators
from base_page import BasePage
from helpers import login_user, register_user, generate_email

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

class TestCreateListing:
    def test_create_listing_unauthorized_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        base_page = BasePage(driver)
        
        base_page.wait_click(HeaderLocators.CREATE_LISTING_BUTTON)
        modal_title = base_page.wait_visible(CreateAdLocators.AUTH_REQUIRED_MODAL)
        assert "авторизуйтесь" in modal_title.text.lower()

    def test_create_listing_authorized_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        login_user(driver)
        
        base_page = BasePage(driver)
        base_page.wait_click(HeaderLocators.CREATE_LISTING_BUTTON)
        
        base_page.wait_visible(CreateAdLocators.TITLE_INPUT).send_keys("Тестовое объявление")
        base_page.wait_visible((By.CSS_SELECTOR, "textarea[placeholder*='Описание']"))
        base_page.wait_visible(CreateAdLocators.PRICE_INPUT).send_keys("1000")
        base_page.wait_visible(CreateAdLocators.CATEGORY_SELECT).click()
        driver.find_element(*CreateAdLocators.CATEGORY_SELECT).send_keys("Электроника")
        base_page.wait_visible(CreateAdLocators.CITY_SELECT).click()
        driver.find_element(*CreateAdLocators.CITY_SELECT).send_keys("Москва")
        base_page.wait_click(CreateAdLocators.CONDITION_NEW)
        base_page.wait_click(CreateAdLocators.PUBLISH_BUTTON)
        
        # Переход в профиль
        base_page.wait_click(HeaderLocators.PROFILE_BUTTON)
        my_ads_title = base_page.find_element(CreateAdLocators.MY_ADS_TITLE)
        assert "Мои объявления" in my_ads_title.text