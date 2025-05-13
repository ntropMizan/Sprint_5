from locators import Authorization, Registration
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_password, generate_email

class TestUserLogout:
    def test_user_logout(self, driver):
        email = generate_email()
        password = generate_password()

        driver.find_element(*Authorization.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Registration.NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Authorization.EMAIL_INPUT)
        ).send_keys(email)

        driver.find_element(*Authorization.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Registration.CONFRIM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Registration.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Authorization.USER_PROFILE_ICON)
        )

        driver.find_element(*Authorization.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(Authorization.USER_PROFILE_ICON)
        )

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Authorization.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()