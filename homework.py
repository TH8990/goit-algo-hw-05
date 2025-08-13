def caching_fibonacci():
    """
    Створює функцію Фібоначчі з кешуванням, використовуючи замикання.
    """
    cache = {}

    def fibonacci(n):
        """
        Обчислює n-те число Фібоначчі з кешуванням.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Використовуємо рекурсію для обчислення та кешування результату.
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання.
fib = caching_fibonacci()
print(fib(10)) 
print(fib(15)) 