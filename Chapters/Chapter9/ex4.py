legal_chars = "acefhlo"
file = open("/Users/mak/Desktop/Git/Education/Think_Python/Chapters/Chapter9/aa.txt", "r")
list_of_words = file.read().split()
file.close()

def uses_only(word: str, allowed_chars: str):
    """
     Проверяет, состоит ли слово только из символов, содержащихся в allowed_chars.

     Возвращает False, если встречается любой символ вне allowed_chars.
     Пустое слово считается допустимым.

     Возвращает:
       True, если все символы слова входят в allowed_chars, иначе False

    Примеры:
        >>> uses_only('hello', 'helo')
        True
        >>> uses_only('hello', 'hel')
        False
        >>> uses_only('', 'abc')
        True
     """
    for char in word:
        if char not in allowed_chars:
            return False
    return True

def good_words(list_of_word: list, good_chars: str):
    """
    Подсчитывает и выводит процент слов, содержащих ТОЛЬКО разрешённые символы.

    Проходит по списку слов и проверяет каждое с помощью функции `uses_only`.
    Результат выводится как процент от общего количества слов и количество подходящих слов.
    Функция ничего не возвращает, только печатает результат

    Пример вывода:
        процент слов использующих только допустимые символы: 0.172%, количество слов: 5
    """
    good_words_count = 0
    for word in list_of_word:
        if uses_only(word, good_chars):
            good_words_count += 1
    print(f'процент слов использующих только допустимые символы: {good_words_count / len(list_of_word) * 100}%, количество слов: {good_words_count}')

good_words(list_of_words, legal_chars)