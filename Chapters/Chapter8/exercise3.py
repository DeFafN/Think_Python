def letter_counter(string, desired_letter):
    count = 0
    for letter in string:
        if letter == desired_letter:
            count = count + 1
    return count
