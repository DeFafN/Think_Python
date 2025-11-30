def check_fermat(a,b,c,n):
    if n > 2:
        if a**n + b**n == c**n:
            return "Cвятые воробьи. Ферма ошибся"
        else:
            return "Не, не работает"

def get_input():
    a = int(input("Введите целое число a: "))
    b = int(input("Введите целое число b: "))
    c = int(input("Введите целое число c: "))
    n = int(input("Введите степень n (должна быть больше 2): "))
    if n <= 2:
        print("Степень должна быть больше 2")
    result = check_fermat(a,b,c,n)
    print(result)

get_input()