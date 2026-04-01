import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = 'https://qa-desk.stand.praktikum-services.ru/'

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()
