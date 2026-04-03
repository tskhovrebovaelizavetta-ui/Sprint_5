import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL, AuthData, AdData, generate_email
from locators.header import HeaderLocators
from locators.registration import RegistrationLocators

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(BASE_URL)
        email = generate_email()
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()
        
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("User")
        driver.find_element(*RegistrationLocators.SURNAME_INPUT).send_keys("Test")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(AuthData.PASSWORD)
        driver.find_element(*RegistrationLocators.PASSWORD_REPEAT_INPUT).send_keys(AuthData.PASSWORD)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        
        user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HeaderLocators.USER_NAME))
        assert "User" in user_name.text

    def test_registration_invalid_email(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()
        
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("invalid-email")
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT))
        assert "error" in email_field.get_attribute("class")

    def test_registration_existing_user(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HeaderLocators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()
        
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Ivan")
        driver.find_element(*RegistrationLocators.SURNAME_INPUT).send_keys("Petrov")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("test@example.com")
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(AuthData.PASSWORD)
        driver.find_element(*RegistrationLocators.PASSWORD_REPEAT_INPUT).send_keys(AuthData.PASSWORD)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        
        error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE))
        assert "Ошибка" in error.text