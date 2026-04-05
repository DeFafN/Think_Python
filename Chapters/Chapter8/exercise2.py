def find(string: str, substring: str) -> int:
    """Возвращает индекс вхождения символа `letter` в строку `string`.


    Возвращает -1, если такого вхождения нет.


    >>> find('abc', 'b')
    2
    >>> find('abc', 'c')
    3
    >>> find('abc', 'd')
    -1
    >>> find('hello', 'll')
    3
    """
    index = 0
    while index < len(string):
        if string[index] == substring[0]:
            return index + 1
        index = index + 1
    return -1