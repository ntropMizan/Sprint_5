from locators import Authorization, AdCreation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_login(driver, authorized_user):
    email = authorized_user["email"]
    password = authorized_user["password"]

    driver.find_element(*Authorization.LOGIN_BUTTON).click()
    driver.find_element(*Authorization.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Authorization.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Authorization.LOGIN_SUBMIT_BUTTON).click()

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
