import time

file = open("../words.txt", "r")  # лучше использовать with

def file_to_dict(file):
    """
    Преобразует файл со словами в словарь, где ключи — это слова, а значения — количество их вхождений.
    Каждая строка файла считается отдельным словом. Пробельные символы по краям удаляются с помощью strip().
    """
    start_time = time.perf_counter()
    words = {}
    for line in file:
        word = line.strip()
        words[word] = words.get(word, 0) + 1
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f'время работы {elapsed_time}')
    return words


def check_word_in_dict(word, words):
    """
    Проверяет, содержится ли заданное слово в словаре.
    """
    return word in words


words = file_to_dict(file)
file.close()

target_word = "zymurgy"
start_time = time.perf_counter()
check_word_in_dict(target_word, words)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Время поиска in: {elapsed_time:.10f}")

def binary_search_dict(d: dict, target_key):
    '''
    Выполняет бинарный поиск по ключу в словаре, используя отсортированный список ключей.
    '''

    sorted_keys = sorted(d.keys())
    left, right = 0, len(sorted_keys) - 1
    while left <= right:
        mid = (left + right) // 2
        current_key = sorted_keys[mid]

        if current_key == target_key:
            return d[current_key]
        elif target_key < current_key:
            right = mid - 1
        else:
            left = mid + 1

    return None

start_time = time.perf_counter()
binary_search_dict(words,target_word)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Время поиска bin: {elapsed_time:.10f}")

# ещё со временем поиска in в списке интересно сравнить