file = open("/Users/mak/Desktop/Git/Education/Think_Python/Chapters/Chapter9/aa.txt", "r")

def file_to_dict(file):
    """
    Преобразует файл со словами в словарь, где ключи — это слова, а значения — количество их вхождений.
    Каждая строка файла считается отдельным словом. Пробельные символы по краям удаляются с помощью strip().
    """
    words = {}
    for line in file:
        word = line.strip()
        words[word] = words.get(word, 0) + 1
    return words

words = file_to_dict(file)
file.close()

def invert_dict(d: dict[K, V]) -> dict[V, list[K]]:
    '''
    Возвращает инвертированный словарь, в котором ключи и значения поменяны местами.
Примеры:
>>> invert_dict({'a': 1, 'b': 2, 'c': 1})
{1: ['a', 'c'], 2: ['b']}

>>> invert_dict({'x': 'y', 'i': 'y', 'z': 'z'})
{'y': ['x', 'i'], 'z': ['z']}

>>> invert_dict({})
{}
    '''

    inverse = dict()
    for key, value in d.items():
        inverse.setdefault(value, []).append(key)
    return inverse

print(invert_dict(words))