import uuid
import random
import string


def generate_email():
    """Генерация случайного email"""
    return f"user_{uuid.uuid4().hex[:8]}@example.com"


def generate_password():
    """Генерация случайного пароля"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))