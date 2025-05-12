from locators import AdCreation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAdPlacementUnauthorized:
    def test_add_unauthorized(self, driver):
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AdCreation.CREATED_AD_BUTTON)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AdCreation.AUTH_MODAL)
        )

        title = driver.find_element(*AdCreation.AUTH_MODAL_TITLE).text
        assert title == "Чтобы разместить объявление, авторизуйтесь"