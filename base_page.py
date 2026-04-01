from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def wait_visible(self, locator):
        """Ожидание видимости элемента"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент не найден: {locator}")
            return None
    
    
        """Ожидание кликабельности с прокруткой"""
    def wait_click(self, locator, timeout=10):
        for attempt in range(3):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                  EC.element_to_be_clickable(locator)
            )
                element.click()
                return
            except StaleElementReferenceException:
                continue
        raise TimeoutException(f"Не удалось кликнуть {locator}")
    
    def find_element(self, *locator):  # ← УБЕРИ args!
        return self.driver.find_element(*locator)

    def go_to(self, url):
        self.driver.get(url)