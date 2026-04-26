def print_long_words(filepath, min_length=20):
    def print_long_words(filepath, min_length=20):
        """
        Читает файл построчно и выводит список слов (или строк), длина которых не меньше заданного значения.

        Предполагается, что каждая строка файла содержит одно слово. Пробельные символы в начале и конце строки
        удаляются перед проверкой длины.

        Параметры:
            filepath (str): путь к текстовому файлу для чтения
            min_length (int): минимальная длина слова для включения в результат (по умолчанию 20)

        Возвращает:
            None: функция ничего не возвращает, только печатает список найденных слов

        Пример использования:
            >>> print_long_words('words.txt', 20)
            ['antidisestablishmentarianism', 'supercalifragilisticexpialidocious']

        Замечание:
            Убедитесь, что файл существует и доступен для чтения. Функция не обрабатывает исключения.
        """
    file = open(filepath, 'r')
    long_words = []
    for line in file:
        if len(line.strip()) >= 20:
            long_words.append(line.strip())
    print(long_words)
