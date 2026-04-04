import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

URL = "https://qa-desk.stand.praktikum-services.ru/"


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()
