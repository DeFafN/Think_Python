def compare(x, y):
    """
Сравнивает два числа и возвращает результат сравнения.

Возвращает:
    1, если x > y
    0, если x == y
   -1, если x < y

Примеры:
    >>> compare(5, 3)
    1
    >>> compare(3, 3)
    0
    >>> compare(2, 5)
    -1
"""
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1