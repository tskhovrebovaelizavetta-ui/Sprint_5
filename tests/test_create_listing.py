import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL, AuthData, AdData, generate_email
from locators.header import HeaderLocators
from locators.create_ad import CreateAdLocators

class TestCreateListing:
    def test_create_listing_unauthorized_user(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.CREATE_LISTING_BUTTON)).click()
        modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CreateAdLocators.AUTH_REQUIRED_MODAL))
        assert "авторизуйтесь" in modal.text.lower()

    def test_create_listing_authorized_user(self, driver):
        driver.get(BASE_URL)
        # Логин
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Email']"))).send_keys("test@example.com")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Пароль']").send_keys("password123")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        
        # Создание объявления
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.CREATE_LISTING_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CreateAdLocators.TITLE_INPUT)).send_keys("Тестовое объявление")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CreateAdLocators.PRICE_INPUT)).send_keys("1000")
        category_input = driver.find_element(*CreateAdLocators.CATEGORY_INPUT)
        category_input.click()
        category_input.send_keys("Электроника")
        
        city_input = driver.find_element(*CreateAdLocators.CITY_INPUT)
        city_input.click()
        city_input.send_keys("Москва")
        
        driver.find_element(*CreateAdLocators.CONDITION_NEW).click()
        driver.find_element(*CreateAdLocators.PUBLISH_BUTTON).click()
        
        # Проверка
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.PROFILE_BUTTON)).click()
        my_ads = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CreateAdLocators.MY_ADS_TITLE))
        assert "Мои объявления" in my_ads.text