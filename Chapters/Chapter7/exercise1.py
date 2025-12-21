import math
def mysqrt(root_expression):
    x = root_expression / 2
    while True:
        y = (x + root_expression / x) / 2
        if y == x:
            break
        x = y
    return x

def test_sqare_root(number):
    print('root_expression', 'mysqrt(root_expression)', 'math.sqrt(root_expression)', 'diff')
    print('-' * 15, '-' * 23, '-' * 25, '-' * 4)
    limit = number * 10
    while number < limit:
        print(f'{number:<15} {mysqrt(number):<23} {math.sqrt(number):<25} {mysqrt(number) - math.sqrt(number):<4}')
        number += 1

test_sqare_root(1)