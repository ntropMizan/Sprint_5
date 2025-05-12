from locators import Registration, Authorization
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import error_border_colors, authorized_user


class TestRegistrationNameVerification:
    def test_existing_user_registration(self, driver):
        email = authorized_user["email"]
        password = authorized_user["password"]

        driver.find_element(*Authorization.LOGIN_BUTTON).click()
        driver.find_element(*Registration.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Authorization.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Authorization.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Registration.CONFRIM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Registration.CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Registration.ERROR_MESSAGE_EMAIL)
        )
        assert error_message.text.strip() == "Ошибка"

        error_fields = [
            driver.find_element(*Registration.EMAIL_FIELD_ERROR),
            driver.find_element(*Registration.PASSWORD_FIELD_ERROR),
            driver.find_element(*Registration.CONFIRM_PASSWORD_FIELD_ERROR)
        ]

        for field in error_fields:
            border_color = field.value_of_css_property("border-color")
            assert any(color in border_color for color in error_border_colors)