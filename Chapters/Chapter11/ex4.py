def has_duplicates(t: list) -> bool:
    """
    Проверяет, содержит ли список дубликаты, используя словарь для отслеживания уже встреченных элементов.

    Функция проходит по списку и добавляет каждый элемент в словарь.
    Если элемент уже есть в словаре — значит, он встречается повторно.

    Параметры:
        t (list): список для проверки на дубликаты

    Возвращает:
        bool: True, если в списке есть хотя бы один дубликат, иначе False

    Примеры:
        >>> has_duplicates([1, 2, 3, 2])
        True
        >>> has_duplicates([1, 2, 3])
        False
        >>> has_duplicates([])
        False
        >>> has_duplicates(['a', 'b', 'a'])
        True
    """
    seen = {}
    for item in t:
        if item in seen:
            return True
        seen[item] = True
    return False