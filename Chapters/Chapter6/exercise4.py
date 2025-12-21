def is_power(base, degree):
    if degree == 1 or base == 1:
        return True
    if degree < base:
        return False
    if degree % base == 0:
        return is_power(base, degree // base)
    else:
        return False