from selenium.webdriver.common.by import By

class RegistrationLocators:
   # Форма логина (2 поля)
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    
    # Форма регистрации (5 поле)
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Имя'] | //input[@name='name']")
    REG_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_REPEAT_INPUT = (By.XPATH, "//input[@name='submitPassword']")
    SURNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Фамилия']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    
    # Ошибки
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Ошибка')]")
    ERROR_INPUT = (By.CSS_SELECTOR, "input[class*='inputStandart'][style*='red']")