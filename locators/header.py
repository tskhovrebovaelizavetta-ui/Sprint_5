from selenium.webdriver.common.by import By

class HeaderLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_LISTING_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_NAME = (By.CSS_SELECTOR, "span.dropDownMenu_textColor__Nyo8k")  
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")