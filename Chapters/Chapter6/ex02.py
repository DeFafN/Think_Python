def fibonacci(n: int) -> int:
    """Возвращает n-ное число в последовательности Фибоначчи"""
    assert n >= 0 , "Число Фиббоначчи не может быть отрицательным"
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
