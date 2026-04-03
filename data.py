import uuid

BASE_URL = 'https://qa-desk.stand.praktikum-services.ru/'


class AuthData:
    """Данные для авторизации и регистрации"""
    PASSWORD = 'Password123!'
    EXISTING_EMAIL = 'lizzza888@yandex.ru'
    EXISTING_PASSWORD = '123'
    USER_NAME = 'User'


class AdData:
    """Данные для создания объявления"""
    AD_TITLE = 'Тестовое объявление'
    AD_PRICE = '1000'
    CATEGORY = 'Электроника'
    CITY = 'Москва'


def generate_email():
    """Генератор уникальных email"""
    return f"ui_autotest_{uuid.uuid4().hex[:10]}@yandex.ru"