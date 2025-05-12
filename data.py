# Базовый URL сайта
BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"


# Авторизованный пользователь для тестов
authorized_user = {
    "email": "user@example.com",
    "password": "SecurePassword123"
}

# Цвета границы поля ввода при ошибке
error_border_colors = ["rgb(255, 0, 0)", "rgb(255, 105, 114)"]


# Невалидные email для проверки формы
invalid_emails = [
    "testemail.com",
    "test@",
    "test.com",
    "test@test",
    " @example.com",
    "test@.com",
    "test@example..com"
]

