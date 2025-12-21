def greatest_common_divisor(divisible1, divisible2):
    if divisible1 == 0:
        return divisible2
    if divisible2 == 0:
        return divisible1
    remainder_of_the_division = divisible1 % divisible2
    if remainder_of_the_division == 0:
        return divisible2
    else:
        divisible1 = divisible2
        divisible2 = remainder_of_the_division
        return greatest_common_divisor(divisible1, divisible2)
