def is_reverse(word1: str, word2: str) -> bool:
    """Проверить, являются ли word1 и word2 обращением друг друга
    >>> is_reverse('порт', 'троп')
    True
    """
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j > -1:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True