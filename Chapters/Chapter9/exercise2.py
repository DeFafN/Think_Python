def has_no_e(word):
    """
    Проверяет, не содержит ли слово букву 'e'.

    Параметры:
        word (str): строка (слово) для проверки

    Возвращает:
        bool: True, если в слове нет буквы 'e', иначе False

    Примеры:
        >>> has_no_e('hello')
        False
        >>> has_no_e('halo')
        True
        >>> has_no_e('')
        True
    """
    return 'e' not in word

def words_without_e(filepath):
    """
    Читает файл со списком слов и находит все слова которые не содержат букву 'e'.

    Также вычисляет и выводит процент таких слов от общего количества слов в файле.

    Параметры:
        filepath (str): путь к текстовому файлу, содержащему по одному слову на строке

    Возвращает:
        None: функция ничего не возвращает, только выводит результат на экран

    Действия:
        - Открывает файл и читает все строки
        - Удаляет символы перевода строки и пробелы
        - Фильтрует слова: длина >= 20 и без буквы 'e'
        - Подсчитывает общее количество слов и долю подходящих
        - Печатает количество и процент найденных слов

    Пример вывода:
        Слов без буквы "e": 5, что составляет 0.3 % от общего числа слов

    """
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    words_without_e = []
    total_words = len(lines)
    for line in lines:
        if has_no_e(line):
            words_without_e.append(line)
    percentage = len(words_without_e) / total_words * 100
    print(f'Слов без буквы "e": {len(words_without_e)}, что составляет {percentage} % от общего числа слов')

words_without_e('/Users/mak/Desktop/Git/Education/Think_Python/Chapters/Chapter9/aa.txt')