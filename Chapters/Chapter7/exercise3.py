import math

def estimate_pi():
    sum_total = 0
    count = 0
    multiplier = 2 * math.sqrt(2) / 9801
    while True:
        numerator = math.factorial(4*count) * (1103 + 26390*count)
        denominator = math.factorial(count)**4 * 396**(4*count)

        sum_total += numerator / denominator
        summand = multiplier * numerator/denominator

        if abs(summand) < 1e-15:
            break
        count += 1

    return 1 / (multiplier * sum_total)