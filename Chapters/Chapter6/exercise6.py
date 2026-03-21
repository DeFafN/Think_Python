def greatest_common_divisor(a: int, b: int) -> int:
    """
    Возвращает наибольший общий делитель (НОД) двух чисел по алгоритму Евклида.

    Параметры:
        a (int): первое целое число
        b (int): второе целое число

    Возвращает:
        int: НОД(a, b)

    Примеры:
        >>> greatest_common_divisor(48, 18)
        6
        >>> greatest_common_divisor(17, 13)
        1
    """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(48, 18))