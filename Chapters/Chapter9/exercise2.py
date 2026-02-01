def has_no_e(word):
    return 'e' not in word

def long_words_without_e(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    long_words = []
    total_words = len(lines)
    for line in lines:
        if len(line) >= 20 and has_no_e(line):
            long_words.append(line)
    percentage = len(long_words) / total_words * 100
    print(f'Слов длиннее 20 символов и без буквы "e": {len(long_words)}, что составляет {percentage} % от общего числа слов')

long_words_without_e('/Users/mak/Desktop/Git/Education/Think_Python/Chapters/Chapter9/aa.txt')