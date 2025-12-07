# Exercise 1.1 Chapter 1
print('Hello World') # выводит в консоль Hello World
print ('Hello World' # приведёт к ошибке syntax error
print 'Hello World' # приведёт к ошибке syntax error SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(Hello World') # приведёт к ошибке SyntaxError: unterminated string literal (detected at line 4)
print(Hello World) # приведёт к ошибке SyntaxError: invalid syntax. Perhaps you forgot a comma?
-2 # игнорируется
print(-2) # выводит в консоль -2
print(2++2) # выводит в консоль 4
print(2+-2) # выводит в консоль 0
print(02) # приведёт к ошибке SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
print(2 0) #приведёт к ошибке SyntaxError: invalid syntax

# Exercise 1.2 Chapter 1
print(42*60+42) # выводит в консоль 2562 (Сколько секунд в 42 минутах и 42 секундах?)
print(10/1.61) # выводит в консоль 6.211180124223602 (Сколько километров в 10 милях?)
print(2562/6.21) # выводит в консоль 412.56038647342996 (количество секунд затраченных на преодоление 1 мили)
print(6.21/(2562/60/60)) # выводит в консоль 8.725995316159251 (скорость в милях в час)