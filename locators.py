from selenium.webdriver.common.by import By

class Authorization:
    #Авторизация
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and contains(text(), 'Вход и регистрация')]")
    EMAIL_INPUT = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Введите Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Пароль']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    USER_PROFILE_ICON = (By.XPATH, "//*[contains(@class, 'svgSmall')]")
    USER_PROFILE_NAME = (By.XPATH, "//h3[contains(@class, 'profileText name')]")
    PROFILE_BUTTON = (By.XPATH, "//button[contains(@class, 'circleSmall')]")


class Registration:
    #Создание аккаунта
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and contains(text(), 'Нет аккаунта')]")
    CONFRIM_PASSWORD_INPUT = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Повторите пароль']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")

    #Ошибки
    ERROR_MESSAGE_EMAIL = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")
    EMAIL_FIELD_ERROR = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(1) div div")
    PASSWORD_FIELD_ERROR = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(2) div div")
    CONFIRM_PASSWORD_FIELD_ERROR = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(3) div div")


class AdCreation:
    CREATED_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    TITLE_FIELD = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Название']")

    # Дропдаун категории
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw input[name='category']")
    CATEGORY_DROPDOWN_BUTTON = (By.CSS_SELECTOR, "button.dropDownMenu_arrowDown__pfGL1")
    CATEGORY_OPTION_BOOKS = (By.XPATH, "//span[contains(@class, 'dropDownMenu_textColor__Nyo8k') and text()='Книги']")
    CATEGORY_OPTION_AUTO = (By.XPATH, "//span[contains(@class, 'dropDownMenu_textColor__Nyo8k') and text()='Авто']")
    CATEGORY_OPTION_GARDENING = (By.XPATH, "//span[contains(@class, 'dropDownMenu_textColor__Nyo8k') and text()='Садоводство']")
    CATEGORY_OPTION_HOBBY = (By.XPATH, "//span[contains(@class, 'dropDownMenu_textColor__Nyo8k') and text()='Хобби']")
    CATEGORY_OPTION_TECHNOLOGY = (By.XPATH, "//span[contains(@class, 'dropDownMenu_textColor__Nyo8k') and text()='Технологии']")

    # Дропдаун город
    CITY_DROPDOWN_BUTTON = (By.XPATH, "//input[@name='city']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")  # Кнопка для открытия списка
    CITY_DROPDOWN = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw input[name='city']")  # Поле с выбранным городом

    #Города
    CITY_OPTION_MOSCOW = (By.XPATH, "//span[text()='Москва']")
    CITY_OPTION_SPB = (By.XPATH, "//span[text()='Санкт-Петербург']")
    CITY_OPTION_NOVOSIBIRSK = (By.XPATH, "//span[text()='Новосибирск']")
    CITY_OPTION_EKATERINBURG = (By.XPATH, "//span[text()='Екатеринбург']")
    CITY_OPTION_NIZHNY_NOVGOROD = (By.XPATH, "//span[text()='Нижний Новгород']")
    CITY_OPTION_KANY = (By.XPATH, "//span[text()='Казань']")

    #Состояние товара
    CONDITION_USED = (By.XPATH, "//div[contains(@class, 'radioUnput_inputRegular__FbVbr')]/following-sibling::label[text()='Б/У']")
    CONDITION_NEW = (By.XPATH, "//div[contains(@class, 'radioUnput_inputActive__eC-HY')]/following-sibling::label[text()='Новый']")

    #Описание товара и цена
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_FIELD = (By.CSS_SELECTOR, "input[name='price']")

    #Публикация товара
    SUBMIT_AD_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

    #Мои объявления
    MY_ADS_SECTION = (By.XPATH, "//h1[text()='Мои объявления']")
    MY_ADS_ITEM = (By.XPATH, "//div[contains(@class, 'description')]")  # Контейнер объявления
    AD_TITLE = (By.XPATH, "//div[contains(@class, 'about')]//h2")  # Название объявления
    AD_CITY = (By.XPATH, "//div[contains(@class, 'about')]//h3")  # Город объявления
    AD_PRICE = (By.XPATH, "//div[contains(@class, 'price')]//h2")  # Цена объявления
    EDIT_BUTTON = (By.CSS_SELECTOR, "button.editButton")  #кнопка редактирования

    #Модалка не авторизованного пользователся
    AUTH_MODAL = (By.CSS_SELECTOR, "form.popUp_shell__LuyqR")  # Контейнер модального окна
    AUTH_MODAL_TITLE = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")  # Заголовок формы