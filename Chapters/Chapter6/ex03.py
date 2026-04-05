def ack(m: int, n: int):
    '''Вычисляет функцию Аккермана'''
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

print(ack(3, 6)) # при m = 4, n = 7 достигается максимальная глубина рекурсии