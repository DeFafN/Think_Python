def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return 'Нет'
    else:
        return 'Да'


def user_input():
    a = int(input('Введите длину первого отрезка: '))
    b = int(input('Введите длину второго отрезка: '))
    c = int(input('Введите длину третьего отрезка: '))
    result = is_triangle(a, b, c)
    print(result)

user_input()