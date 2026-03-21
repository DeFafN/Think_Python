def is_power(base: int, degree: int) -> bool:
    """
    Проверяет, является ли число `degree` степенью числа `base`.

    Использует рекурсивный подход: если `degree` делится на `base`,
    проверяем `degree // base`, и так до тех пор, пока не дойдём до 1.

    Параметры:
        base (int): основание степени (должно быть > 0)
        degree (int): проверяемое число (должно быть >= 1)

    Возвращает:
        bool: True, если `degree` — это `base^n` для некоторого n >= 0, иначе False
    """
    # Базовые случаи
    if degree == 1:
        return True  # base^0 = 1 для любого base ≠ 0
    if base == 1:
        return degree == 1  # 1^n = 1, иначе не степень
    if degree < base:
        return False  # если degree < base, оно не может быть его степенью
    if degree % base != 0:
        return False  # если не делится нацело — не степень

    # Рекурсивный случай
    return is_power(base, degree // base)