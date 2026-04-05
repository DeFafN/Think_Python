def any_lowercase1(s: str):
    """
    Проверяет, является ли первый символ строки строчной буквой.

    Проходит по строке и возвращает True при первом встреченном строчном символе.
    Если первый символ не строчный, сразу возвращается False, даже если дальше есть строчные.

    Возвращает:
        bool: True, если первый символ — строчная буква, иначе False

    Примеры:
        >>> any_lowercase1('Hello')
        False
        >>> any_lowercase1('hello')
        True
        >>> any_lowercase1('123')
        False
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s: str):
    """
    НЕПРАВИЛЬНАЯ функция: всегда возвращает строку 'True'.

    Содержит ошибку: проверяется не символ строки, а строка 'c', которая всегда в нижнем регистре.
    Возвращает строки 'True'/'False', а не булевы значения. Работает некорректно.

    Возвращает:
        str: всегда возвращает 'True'

    Примеры:
        >>> any_lowercase2('HELLO')
        'True'
        >>> any_lowercase2('Вася')
        'True'
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s: str):
    """
    Возвращает результат проверки последнего символа строки на строчную букву.

    Переменная flag перезаписывается на каждом шаге. В итоге возвращается значение
    islower() только для последнего символа, независимо от остальных.

    Возвращает:
        bool: True, если последний символ — строчная буква, иначе False

    Примеры:
        >>> any_lowercase3('heLLo')
        True
        >>> any_lowercase3('hellO')
        False
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s: str):
    """
    Правильно определяет, содержит ли строка хотя бы один строчный символ.

    Использует логическое ИЛИ для накопления результата. Если хотя бы один символ
    в нижнем регистре, флаг становится True и остаётся таким до конца.

    Возвращает:
        bool: True, если в строке есть хотя бы одна строчная буква, иначе False

    Примеры:
        >>> any_lowercase4('HELlo')
        True
        >>> any_lowercase4('HELLO')
        False
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s: str):
    """
    Проверяет, состоят ли все символы строки из строчных букв.

    Возвращает False при первом же символе, который не является строчным (заглавный, цифра, знак).
    По сути — противоположность isupper(), но с учётом не-букв.

    Возвращает:
        bool: True, если все символы — строчные буквы, иначе False

    Примеры:
        >>> any_lowercase5('hello')
        True
        >>> any_lowercase5('hello123')
        False
        >>> any_lowercase5('heLlo')
        False
    """
    for c in s:
        if not c.islower():
            return False
    return True