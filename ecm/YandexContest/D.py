def only_positive_even_sum(a, b):

    if not type(a) == type(b) == int:
        raise TypeError()

    elif a % 2 != 0 or a < 0 or b % 2 != 0 or b < 0:
        raise ValueError()

    else:
        return a + b