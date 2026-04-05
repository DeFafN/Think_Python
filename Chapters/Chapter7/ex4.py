def first(word: str) -> str:
    """Возвращает первый символ строки"""
    return word[0]

def last(word: str) -> str:
    """Возвращает последний символ строки"""
    return word[-1]

def middle(word: str) -> str:
    """Возвращает строку без первой и последней буквы"""
    return word[1:-1]

def is_palindrome(word: str) -> bool:
    """
    Проверяет, является ли строка палиндромом, используя цикл while.

    Возвращает:
        bool: True, если строка — палиндром, иначе False
    """
    s = word.replace(" ", "").lower()  # удаляем пробелы из строки и приводим к нижнему регистру, чтобы не учитывать регистр букв в палиндроме).lower()  # убираем пробелы и приводим к нижнему регистру

    while len(s) > 1:
        if first(s) != last(s):
            return False
        s = middle(s)
    return True