def first(word: str) -> str:
    """Возвращает первый символ строки"""
    return word[0]
def last(word: str) -> str:
    """Возвращает последний символ строки"""
    return word[-1]
def middle(word: str) -> str:
    """Возвращает строку без первой и последней буквы"""
    return word[1:-1] #при длине меньше 3 символов, вернёт пустую строку

print(middle("te"))