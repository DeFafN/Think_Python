def reverse_string(string):
    index = len(string) - 1
    while index != -1:
        print(string[index])
        index -= 1

reverse_string("Hello")
