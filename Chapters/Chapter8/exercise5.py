def rotate_word(word, shift):
    rotated = ""
    for char in word:
        if shift == 0:
            return word
        elif 'a' <= char <= 'z':
            base = ord('a')
            rotated += chr((ord(char) - base + shift) % 26 + base)
        elif 'A' <= char <= 'Z':
            base = ord('A')
            rotated += chr((ord(char) - base + shift) % 26 + base)
        elif 'а' <= char <= 'я':
            base = ord('а')
            rotated += chr((ord(char) - base + shift) % 33 + base)
        elif 'А' <= char <= 'Я':
            base = ord('А')
            rotated += chr((ord(char) - base + shift) % 33 + base)
        else:
            rotated += char
    return rotated

print(rotate_word("zayac", 2))      # Латиница → bcace
print(rotate_word("заяц", 2))       # Кириллица → йвбч
print(rotate_word("Hello Привет", 3)) # Смешанный текст