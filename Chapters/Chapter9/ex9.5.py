required_chars = "aeiou"
required_chars2 = 'aeiouy'
file = open("/Users/mak/Desktop/Git/Education/Think_Python/Chapters/Chapter9/aa.txt", "r")
list_of_words = file.read().split()
file.close()

def uses_all(word: str, required_chars: str):
    """
  Проверяет, содержит ли слово ВСЕ указанные символы (каждый хотя бы раз).

  True, если слово содержит все символы из required_chars, иначе False

  Примеры:
      >>> uses_all('education', 'aeiou')
      True
      >>> uses_all('hello', 'aeiou')
      False
  """
    for char in required_chars:
        if char not in word:
            return False
    return True

def allowed_words(list_of_words: list, required_chars: str):
    """
    Подсчитывает количество слов, содержащих все заданные символы, и выводит процент от общего числа.
    Функция печатает результат
    """
    count_of_words = 0
    for word in list_of_words:
        if uses_all(word, required_chars):
            count_of_words += 1
    print(f"Количество слов с заданными буквами: {count_of_words}, что составляет {count_of_words / len(list_of_words) * 100}%")

allowed_words(list_of_words, required_chars)
allowed_words(list_of_words, required_chars2)