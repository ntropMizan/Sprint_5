from locators import Registration, Authorization, AdCreation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration_and_profile_name(driver, generate_email, generate_password):
    email = generate_email
    password = generate_password

    driver.find_element(*Authorization.LOGIN_BUTTON).click()

    driver.find_element(*Registration.NO_ACCOUNT_BUTTON).click()
    driver.find_element(*Authorization.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Authorization.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Registration.CONFRIM_PASSWORD_INPUT).send_keys(password)

    driver.find_element(*Registration.CREATE_ACCOUNT_BUTTON).click()

    # Отображение аватара
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Authorization.USER_PROFILE_ICON)
    )

    # Наличие кнопки "Разместить объявление"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AdCreation.CREATED_AD_BUTTON)
    )
    # Отображение имени
    user_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Authorization.USER_PROFILE_NAME)
    ).text

    assert user_name == "User."