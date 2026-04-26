file = open("/Users/mak/Desktop/Git/Education/Think_Python/Chapters/Chapter9/aa.txt", "r")
list_of_words = file.read().split()
file.close()

def is_abecedarian(word: str):
    """
  Проверяет, идут ли все буквы в слове в алфавитном порядке.

  Функция сравнивает каждую букву слова с предыдущей. Если текущая буква меньше
  по алфавиту, чем предыдущая — порядок нарушен, возвращается False.
  Слова из одной буквы или пустые строки считаются корректными.

  Возвращает:
      True, если буквы в слове упорядочены по алфавиту, иначе False

  Примеры:
      >>> is_abecedarian('abc')
      True
      >>> is_abecedarian('abdca')
      False
      >>> is_abecedarian('a')
      True
      >>> is_abecedarian('')
      True
  """
    for index in range(1, len(word)):
        if word[index] < word[index - 1]:
            return False
    return True

def count_abecedarian(list_of_words: list):
    """
    Подсчитывает и выводит процент слов, в которых буквы идут в алфавитном порядке.

    Проходит по списку слов и проверяет каждое с помощью функции `is_abecedarian`.
    Результат выводится в процентах с округлением до двух знаков после запятой.

    Функция ничего не возвращает, только печатает результат

    Пример вывода:
        Процент слов в которых буквы идут в алфавитном порядке: 0.53%
    """
    count_of_words = 0
    for word in list_of_words:
        if is_abecedarian(word):
            count_of_words += 1
    print(f'Процент слов в которых буквы идут в алфавитном порядке: {round(count_of_words / len(list_of_words) * 100, 2)}%')

count_abecedarian(list_of_words)