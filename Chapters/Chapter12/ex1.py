def sumall(*args: int) -> int:
    ''' возвращает сумму всех целочисленных аргументов
    >>> sumall(1, 2, 3)
    6
    >>> sumall()
    0
    >>> sumall(3,5,-1)
    7
    '''
    sum_of_numbers = sum(args)
    return sum_of_numbers


