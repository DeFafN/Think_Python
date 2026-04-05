def letter_counter(string, desired_letter):
    """
    Подсчитывает количество вхождений указанной буквы в строке.

    Возвращает:
        int: количество раз, сколько `desired_letter` встречается в `string`

    Примеры:
        >>> letter_counter('банан', 'а')
        2
        >>> letter_counter('Привет, Мир!', 'и')
        2
        >>> letter_counter('hello', 'l')
        2
        >>> letter_counter('hello', 'x')
        0

    """
    count = 0
    for letter in string:
        if letter.lower() == desired_letter.lower():
            count = count + 1
    return count
