def is_palindrome(word: str):
    '''Проверяет является ли слово палиндромом (читается одинаково с начала и с конца)'''
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
