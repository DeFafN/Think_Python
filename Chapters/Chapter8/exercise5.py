def is_palindrome(word: str):
    """
    Проверяет, является ли строка палиндромом.

    Возвращает:
        bool: True, если строка — палиндром, иначе False

    Примеры:
        >>> is_palindrome("шалаш")
        True
        >>> is_palindrome("привет")
        False
        >>> is_palindrome("абба")
        True
        >>> is_palindrome("А роза упала на лапу Азора")
        False

    Замечание:
        Эта реализация чувствительна к пробелам и знакам препинания.
    """
    if word.lower() == word.lower()[::-1]:
        return True
    else:
        return False
