from locators import Authorization, AdCreation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import authorized_user


class TestAdPlacement:
    def test_add_placement(self, driver):
        email = authorized_user["email"]
        password = authorized_user["password"]

        # Авторизация
        driver.find_element(*Authorization.LOGIN_BUTTON).click()
        driver.find_element(*Authorization.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Authorization.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Authorization.LOGIN_SUBMIT_BUTTON).click()

        # Ожидание загрузки профиля
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Authorization.USER_PROFILE_NAME)
        )

        # Переход к созданию объявления
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(AdCreation.CREATED_AD_BUTTON)
        ).click()

        # Заполнение заголовка объявления
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdCreation.TITLE_FIELD)
        ).send_keys('Жигули')

        # Выбор категории "Автомобили"
        driver.find_element(*AdCreation.CATEGORY_DROPDOWN_BUTTON).click()
        driver.find_element(*AdCreation.CATEGORY_OPTION_AUTO).click()

        # Выбор города "Новосибирск"
        driver.find_element(*AdCreation.CITY_DROPDOWN_BUTTON).click()
        driver.find_element(*AdCreation.CITY_OPTION_NOVOSIBIRSK).click()

        # Проверка выбранного города
        selected_city = driver.find_element(*AdCreation.CITY_DROPDOWN).get_attribute("value")

        # Выбор состояния "Б/У"
        driver.find_element(*AdCreation.CONDITION_USED).click()

        # Добавление описания и цены
        driver.find_element(*AdCreation.DESCRIPTION_FIELD).send_keys("Полностью на ходу, но не факт")
        driver.find_element(*AdCreation.PRICE_FIELD).send_keys('500000000')

        # Публикация объявления
        driver.find_element(*AdCreation.SUBMIT_AD_BUTTON).click()

        # Переход в профиль пользователя
        driver.find_element(*Authorization.PROFILE_BUTTON).click()

        # Ожидание появления объявления в "Мои объявления"
        my_ads_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AdCreation.MY_ADS_ITEM)
        )

        # Проверка, что объявление отображается
        assert my_ads_item.is_displayed()