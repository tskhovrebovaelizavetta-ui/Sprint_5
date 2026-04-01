import uuid

BASE_URL = 'https://qa-desk.stand.praktikum-services.ru/'
PASSWORD = 'Password123!'
EXISTING_EMAIL = 'test_user@example.com'
EXISTING_PASSWORD = 'Password123!'
USER_NAME = 'User'
AD_TITLE = 'Автотест объявление'
AD_DESCRIPTION = 'Описание товара для UI автотеста'
AD_PRICE = '1500'
CATEGORY = 'Хобби'
CITY = 'Казань'
CONDITION_TEXT = 'Новый'
UNMASKED_EMAIL = 'invalid_email'

def generate_email():
    return f"ui_autotest_{uuid.uuid4().hex[:10]}@yandex.ru"
