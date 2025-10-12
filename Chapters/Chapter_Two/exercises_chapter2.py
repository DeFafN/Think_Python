# Exercise 2.1 Chapter 2
n = 42
#42 = n # SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
x = y = 1 #присваивает значение 1 переменным x и y
print(x,y) #выводит значения переменных x и y
x = y = 1; # ; не приводит к ошибке
#print(x,y). # SyntaxError: invalid syntax
#print(xy) #NameError: name 'xy' is not defined. Did you mean: 'x'?


# Exercise 2.2 Chapter 2
# радиус сферы
r = 5 # радиус
pi = 3.14 # число пи
v = 4/3 * pi * r**3 # объём сферы
print(v) #523.3333333333334

# стоимость 60 книг с доставкой
book_price = 249.5
discount = 0.4
delivery_price_of_first_book = 100
delivery_price_of_other_books = 49.5
number_of_books = 60
total_price = book_price*number_of_books
discount_value = total_price*discount
price_with_discount = total_price-discount_value
delivery_price = (delivery_price_of_first_book + delivery_price_of_other_books*(number_of_books-1))
total_cost = price_with_discount + delivery_price
print(total_cost)
#12002.5

# Время завтрака
easy_runtime_seconds = (8 * 60 + 15)*2
middle_runtime_seconds = (7 * 60 + 12)*3
total_runtime = easy_runtime_seconds + middle_runtime_seconds
total_runtime_minutes = total_runtime // 60

start_hour = 6
start_minute = 52
start_time = start_hour * 60 + start_minute

final_time = start_time + total_runtime_minutes
final_hour = final_time // 60
final_minute = final_time % 60
print(final_hour, final_minute) #7  30