from selenium.webdriver.common.by import By


class HeaderLocators:
    BUTTON_LOGIN_REG = (By.XPATH, "//button[text()='Вход и регистрация']")
    BUTTON_PLACE_AD = (By.XPATH, "//button[text()='Разместить объявление']")
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выйти']")
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.CLASS_NAME, "profileText")


class LoginPopupLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
    BUTTON_NO_ACCOUNT = (By.XPATH, "//button[text()='Нет аккаунта']")


class RegisterPopupLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "span[class*='input_span']")
    INPUT_ERROR = (By.CSS_SELECTOR, "div[class*='input_inputError']")


class ModalLocators:
    MODAL_TITLE = (By.CSS_SELECTOR, "div[class*='popUp_titleRow'] h1")


class CreateAdLocators:
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Название']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
    CATEGORY_ARROW = (By.XPATH, "(//div[contains(@class, 'dropDownMenu_dropMenu')])[1]//button")
    CITY_ARROW = (By.XPATH, "(//div[contains(@class, 'dropDownMenu_dropMenu')])[2]//button")
    BUTTON_PUBLISH = (By.XPATH, "//button[text()='Опубликовать']")
    RADIO_NEW = (By.XPATH, "//div[contains(@class, 'radioUnput_shell')]")


class DropdownOptionLocators:
    @staticmethod
    def category_option(text):
        return (By.XPATH, f"(//div[contains(@class, 'dropDownMenu_dropMenu')])[1]//span[text()='{text}']")

    @staticmethod
    def city_option(text):
        return (By.XPATH, f"(//div[contains(@class, 'dropDownMenu_dropMenu')])[2]//span[text()='{text}']")


class ProfileLocators:
    PROFILE_LINK = (By.CSS_SELECTOR, "button.circleSmall")
    AD_CARD = (By.CLASS_NAME, "card")
