import pytest
from selenium import webdriver
from data import BASE_URL


@pytest.fixture
def driver():
    """Фикстура для инициализации WebDriver"""
    driver = webdriver.Chrome()
    driver.get(BASE_URL)  # Открываем сайт сразу после инициализации
    yield driver  # Передача driver в тест
    driver.quit()  # Завершение работы после теста
