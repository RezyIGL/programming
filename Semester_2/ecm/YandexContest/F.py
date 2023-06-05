class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c):

    if a == 0 and b == 0 and c == 0:
        raise InfiniteSolutionsError

    if a == 0 and b == 0 and c != 0:
        raise NoSolutionsError

    d = b * b - 4 * a * c

    if d < 0:
        raise NoSolutionsError

    else:
        return (-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a) 