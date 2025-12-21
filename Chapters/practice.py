
# сумма с моржом
summ = 0
while (number := int(input('Enter a number: '))) != 0:
    summ = summ + number
print(summ)

# сумма обычная
summ = 0
while True:
    number = int(input('Enter a number: '))
    if number == 0:
        break
    summ = summ + number


string = "Hello, World!"

#печать строки циклом for
for i in string:
    print(i)

# печать строки циклом while
length = len(string)
i = 0
while i < length:
    print(string[i])
    i += 1


# ищем символ в строке (важно приводить к одному регистру, upper или lower)
count = 0
for symbol in string:
    if symbol == 'o':
        count += 1
print(count)

#сравнение строк
string1 = "Hello"
string2 = "World"
print(string1 > string2) # False
print(string1 < string2) # True
# Сравнивает по таблице кодировок символов

#оператор in
'a' in "Hello" '-> False'
'e' in "Hello" '-> True'

# Ищем повторяющиеся буквы
def is_only_doubles(string):
    length = len(string)
    i = 0
    while i < length:
        if string[i] != 'a':
            i += 1

        elif string[i+1] == 'a':
            i += 2
        else:
            return False
    return True
print(is_only_doubles("abcghsljlgaa"))
print(is_only_doubles("bcghfhjlgaaf"))
print(is_only_doubles(""))
print(is_only_doubles("b"))
print(is_only_doubles("a"))