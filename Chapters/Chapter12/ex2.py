def print_most_frequent(string: str) -> tuple:
    """
    Анализирует строку и возвращает символы, отсортированные по убыванию частоты встречаемости.
    Возвращает кортеж, содержащий пары (частота, список_символов),
    отсортированный в порядке убывания частоты.

    Примеры:
        >>> print_most_frequent("hello")
        ((2, ['l']), (1, ['h', 'e', 'o']))

        >>> print_most_frequent("aabbcc")
        ((2, ['a', 'b', 'c']),)

        >>> print_most_frequent("")
        ()
        >>> print_most_frequent("abracadabra")
        ((5, ['a']), (2, ['b', 'r']), (1, ['c', 'd']))
    """
    dict_of_chars = {}
    for char in string:
        if char not in dict_of_chars:
            dict_of_chars[char] = 1
        else:
            dict_of_chars[char] += 1
    reversed_dict_of_chars = {}
    for key, value in dict_of_chars.items():
        if value not in reversed_dict_of_chars:
            reversed_dict_of_chars[value] = [key]
        else:
            reversed_dict_of_chars[value].append(key)
    chars_and_frequent = tuple(reversed_dict_of_chars.items())

    return tuple(sorted(chars_and_frequent, reverse=True))

print(print_most_frequent("hello world"))