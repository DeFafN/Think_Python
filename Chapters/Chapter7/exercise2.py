def eval_loop():
    while True:
        user_input = input("Введите выражение: ")
        if user_input == 'Готово':
            print(f"Последний результат: {result}")
            break
        result = eval(user_input)
        print(f"Результат: {result}")

