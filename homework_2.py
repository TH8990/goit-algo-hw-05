import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генерує числа з плаваючою точкою з рядка.
    """
    # Регулярний вираз для пошуку чисел, розділених пробілами.
    pattern = r'\s\d+\.\d+\s' # Замість r'\b\d+\.\d+\b' 
    numbers_as_strings = re.findall(pattern, text)
    
    for num_str in numbers_as_strings:
        # Видаляємо пробіли, які знайшов findall, і перетворюємо на float.
        yield float(num_str.strip())

def sum_profit(text: str, func: Callable):
    """
    Обчислює суму чисел, згенерованих наданою функцією.
    """
    total_sum = 0
    # Аргумент func є генератором, ми можемо ітеруватися по ньому.
    for number in func(text):
        total_sum += number
    return total_sum

# Приклад використання.
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") 