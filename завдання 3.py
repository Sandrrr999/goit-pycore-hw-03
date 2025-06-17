import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр
    digits = re.sub(r'\D', '', phone_number)

    # Якщо номер починається з '380', додаємо тільки '+'
    if digits.startswith('380'):
        return '+' + digits
    # Якщо номер починається з '0', додаємо '+38'
    elif digits.startswith('0'):
        return '+38' + digits
    # Якщо вже є міжнародний код (наприклад, '44...'), додаємо '+'
    else:
        return '+38' + digits
