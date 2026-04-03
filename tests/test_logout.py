import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL, AuthData, AdData, generate_email
from locators.header import HeaderLocators

class TestLogout:
    def test_logout_user(self, driver):
        driver.get(BASE_URL)
        # Логин
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Email']"))).send_keys(AuthData.EXISTING_EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Пароль']").send_keys(AuthData.EXISTING_PASSWORD)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HeaderLocators.USER_NAME))
        
        # Логаут
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON))
        assert len(driver.find_elements(*HeaderLocators.USER_NAME)) == 0