from locators import Registration, Authorization
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_email(driver, generate_password, error_border_colors):

    password = generate_password
    # Открытие формы регистрации
    driver.find_element(*Authorization.LOGIN_BUTTON).click()
    driver.find_element(*Registration.NO_ACCOUNT_BUTTON).click()

    # Ввод некорректного email и паролей
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Authorization.EMAIL_INPUT)
    ).send_keys('testemail.com')

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Authorization.PASSWORD_INPUT)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Registration.CONFRIM_PASSWORD_INPUT)
    ).send_keys(password)

    driver.find_element(*Registration.CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Registration.ERROR_MESSAGE_EMAIL)
    )

    error_fields = [
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Registration.EMAIL_FIELD_ERROR)),
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Registration.PASSWORD_FIELD_ERROR)),
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Registration.CONFIRM_PASSWORD_FIELD_ERROR))
    ]

    for field in error_fields:
        border_color = field.value_of_css_property("border-color")
        assert any(color in border_color for color in error_border_colors)