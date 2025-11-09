#Exercise3.1 Chapter 3

string = input('Введите строку: ')
def right_justify(string):
        print(' ' * (70 - len(string)) + string)
right_justify(string)

#Exercise3.2 Chapter 3

def print_spam():
    print('спам')

def do_twice(func, value):
    print_spam()
    print_spam()

def print_twice(text):
    print(text)
    print(text)

def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)

do_four(do_twice, 'Спам')

#Exercise3.3 Chapter 3
def print_raw():
    print('+ ', '- '*4, '+', end='')
    print(' ', '- '*4, '+')
def print_colum():
    print('|', ' '*9, '|', ' '*9, '|')

print_raw()
print_colum()
print_colum()
print_colum()
print_raw()
print_colum()
print_colum()
print_colum()

#grid 4x4
raw = '+ ' + 4 * '- '
colum = '|' + 9 * ' '

def print_plus_minus(raw):
    print(3 * raw + "+", sep='',)

def print_line(colum):
    print(3* colum + '|', sep='')

def do_twice(func, value):
    func(value)
    func(value)

def print_spam(text):
    print(text)

def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)

print_plus_minus(raw)
do_four(print_line, colum)
print_plus_minus(raw)
do_four(print_line, colum)
print_plus_minus(raw)
do_four(print_line, colum)
print_plus_minus(raw)
do_four(print_line, colum)
print_plus_minus(raw)