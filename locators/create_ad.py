from selenium.webdriver.common.by import By

class CreateAdLocators:
    # Главная форма поиска
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    CATEGORY_INPUT = (By.XPATH, "//input[@name='category']")
    CITY_INPUT = (By.XPATH, "//input[@name='city']")
    PRICE_INPUT = (By.XPATH, "//input[@name='price']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[placeholder*='Описание товара']")
    
    # Модалка создания объявления
    TITLE_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Название']")  
    AD_PRICE_INPUT = (By.XPATH, "//input[@name='price']")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    
    # Модалка неавторизованного
    AUTH_REQUIRED_MODAL = (By.XPATH, "//*[contains(text(), 'авторизуйтесь')]")