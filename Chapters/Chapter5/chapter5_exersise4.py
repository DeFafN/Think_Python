def recurse(n, s):
    ''' n - количество рекурсий, s - сумма всех n, когда n == 0, выводится s'''
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

recurse(3, 0)

