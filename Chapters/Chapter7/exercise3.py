import math

def mysqrt(a: float) -> float:
    """
    Вычисляет квадратный корень из числа a методом Ньютона.

    Параметры:
        a (float): число, из которого извлекается квадратный корень (должно быть >= 0)

    Возвращает:
        float: приближённое значение √a

    """
    if a == 0:
        return 0.0
    x = a / 2  # начальное приближение
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 1e-15:  # сходимость достигнута
            break
        x = y
    return y


def print_row(col1, col2, col3, col4):
    """Функция печатает строку таблицы (с четырьмя столбцами).

    Аргументы - значения, которые будут напечатаны в ячейках строки таблицы."""
    template = "{:>3} | {:<20} | {:<20} | {:<20}"
    print(template.format(col1, col2, col3, col4))


def test_mysqrt():
    """
    Печатает таблицу сравнения результатов функции mysqrt() и math.sqrt().

    Столбцы:
      a           — число
      mysqrt(a)   — результат нашей функции
      math.sqrt(a)— результат из стандартной библиотеки
      погрешность — абсолютная разница между ними
    """
    print_row("a", "mysqrt(a)", "math.sqrt(a)", "погрешность")
    print_row("-", "---------", "------------", "-----------")

    for a in range(0, 10):
        my_val = mysqrt(a)
        math_val = math.sqrt(a)
        diff = abs(my_val - math_val)
        print_row(a, f"{my_val:.16g}", f"{math_val:.16g}", f"{diff:.16g}")


# Запуск теста
test_mysqrt()