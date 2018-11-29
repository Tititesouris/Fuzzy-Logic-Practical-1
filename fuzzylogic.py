import numpy as np


def fuzzy_trapezoid(a, b, c, d, x):
    if a < x < b:
        return (x - a) / (b - a)
    if b <= x <= c:
        return 1
    if c < x < d:
        return (d - x) / (d - c)
    return 0


def fuzzy_grades(membership_functions, value):
    return [membership_function(value) for membership_function in membership_functions]


def fuzzy_not(grade):
    return 1 - grade


def fuzzy_or(grade1, grade2):
    return max(grade1, grade2)


def fuzzy_and(grade1, grade2):
    return min(grade1, grade2)


def fuzzy_combine(functions, values):
    if len(functions) == 1:
        return list(map(functions[0], values))

    if len(functions) == 2:
        return list(map(functions[0], fuzzy_combine(functions[1], values)))

    if len(functions) == 3:
        return list(map(functions[0], fuzzy_combine(functions[1], values), fuzzy_combine(functions[2], values)))


def fuzzy_imply(grade, rule, values):
    return [min(grade, rule(value)) for value in values]
