def gratest_common_divisor(a: int, b: int) -> int:
    """
    Возвращает наибольший общий делитель (НОД) двух чисел по алгоритму Евклида.

    Параметры:
        a (int): первое целое число
        b (int): второе целое число

    Возвращает:
        int: НОД(a, b)

    Примеры:
        gratest_common_divisor(48, 18)
        6
        gratest_common_divisor(17, 13)
        1
    """
    if b == 0:
        return a
    return gratest_common_divisor(b, a % b)

print(gratest_common_divisor(48, 18))