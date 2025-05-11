import pytest
from locators import Registration, Authorization
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("invalid_email", [
    "testemail.com",
    "test@",
    "test.com",
    "test@test",
    " @example.com",
    "test@.com",
    "test@example..com"
])
def test_invalid_email_error(driver, generate_password, invalid_email):
    password = generate_password

    # Открытие формы регистрации
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Authorization.LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Registration.NO_ACCOUNT_BUTTON)
    ).click()

    # Заполнение полей
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Authorization.EMAIL_INPUT)
    ).send_keys(invalid_email)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Authorization.PASSWORD_INPUT)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Registration.CONFRIM_PASSWORD_INPUT)
    ).send_keys(password)

    # Отправка формы
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Registration.CREATE_ACCOUNT_BUTTON)
    ).click()

    # Единственный assert для проверки ошибки
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Registration.ERROR_MESSAGE_EMAIL)
    )
    assert error_message.text.strip() == "Ошибка"