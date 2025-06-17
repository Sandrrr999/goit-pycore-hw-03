import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка вхідних даних
    if (not isinstance(min_num, int) or not isinstance(max_num, int) or not isinstance(quantity, int)
        or min_num < 1
        or max_num > 77
        or min_num > max_num
        or quantity > (max_num - min_num + 1)):
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_num, max_num + 1), quantity)

    # Сортування чисел перед поверненням
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 77, 6)
print("Ваші лотерейні числа:", lottery_numbers)
