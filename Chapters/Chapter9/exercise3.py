stopchars = "abcdef"
file = open("/Users/mak/Desktop/Git/Education/Think_Python/Chapters/Chapter9/aa.txt", "r")
list_of_words = file.read().split()
file.close()

def avoids(word: str, forbidden_list:str):
    """
    Проверяет, содержит ли слово запрещённые символы.

    Функция последовательно проверяет каждый символ из `forbidden_list`:
    если хотя бы один из них присутствует в слове, возвращается False.
    Если ни один запрещённый символ не найден — возвращается True.

    Примеры:
        >>> avoids('hello', 'xyz')
        True
        >>> avoids('hello', 'el')
        False
        >>> avoids('world', 'abc')
        True
        >>> avoids('', 'hello')
        True
    """
    for element in forbidden_list:
        if element in word:
            return False
    return True

def non_forbidden_words(list_of_words: list, stopchars: str):
    """
    Подсчитывает и выводит процент слов, не содержащих ни одного из запрещённых символов.

    Использует функцию `avoids()` для проверки каждого слова на наличие запрещённых символов.
    Результат выводится в формате с двумя знаками после запятой.

    Функция ничего не возвращает, только печатает результат

    Пример вывода:
        42.50% слов не содержат запрещенных букв.
    """
    total_words = len(list_of_words)
    good_words = 0
    for word in list_of_words:
        if avoids(word, stopchars):
            good_words += 1
    percentage = good_words / total_words * 100
    print(f"{percentage:.2f}% слов не содержат запрещенных букв.")

non_forbidden_words(list_of_words, stopchars)