import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL, AuthData, AdData, generate_email
from locators.header import HeaderLocators

class TestLogin:
    def test_login_user(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Email']"))).send_keys(AuthData.EXISTING_EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Пароль']").send_keys(AuthData.EXISTING_PASSWORD)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        
        user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HeaderLocators.USER_NAME))
        assert AuthData.USER_NAME in user_name.text