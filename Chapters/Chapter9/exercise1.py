def print_long_words(filepath, min_length=20):
    file = open(filepath, 'r')
    long_words = []
    for line in file:
        if len(line.strip()) >= 20:
            long_words.append(line.strip())
    print(long_words)
