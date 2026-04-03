from selenium.webdriver.common.by import By

class HeaderLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_LISTING_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_NAME = (By.CSS_SELECTOR, "profileText name")  
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    PROFILE_BUTTON = (By.XPATH, "//button[contains(@class, 'profile')]")

   