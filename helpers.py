import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, LoginPopupLocators


def generate_email():
    unique = uuid.uuid4().hex[:8]
    return f"test_{unique}@yandex.ru"


def wait_and_click(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()


def wait_and_send_keys(driver, locator, text, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    element.clear()
    element.send_keys(text)


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_presence(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


def wait_for_invisibility(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )


def login_user(driver, email, password):
    wait_and_click(driver, HeaderLocators.BUTTON_LOGIN_REG)
    wait_and_send_keys(driver, LoginPopupLocators.EMAIL_INPUT, email)
    wait_and_send_keys(driver, LoginPopupLocators.PASSWORD_INPUT, password)
    wait_and_click(driver, LoginPopupLocators.BUTTON_LOGIN)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(HeaderLocators.USER_AVATAR)
    )
