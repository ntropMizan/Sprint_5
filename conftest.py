import pytest
from selenium import webdriver
import uuid
import random
import string


# Базовый URL сайта
BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture
def driver():
    """Фикстура для инициализации WebDriver"""
    driver = webdriver.Chrome()
    driver.get(BASE_URL)  # Открываем сайт сразу после инициализации
    yield driver  # Передача driver в тест
    driver.quit()  # Завершение работы после теста


@pytest.fixture
def generate_email():
    """Генерация случайного email"""
    return f"user_{uuid.uuid4().hex[:8]}@example.com"


@pytest.fixture
def generate_password():
    """Генерация случайного пароля"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))


# conftest.py
@pytest.fixture(scope="session")
def error_border_colors():
    return ["rgb(255, 0, 0)", "rgb(255, 105, 114)"]


@pytest.fixture
def authorized_user():
    return {
        "email": "user@example.com",
        "password": "SecurePassword123"
    }


