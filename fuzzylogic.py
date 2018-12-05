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


def fuzzy_imply_mamdani(grade, rule, values):
    return [min(grade, rule(value)) for value in values]


def fuzzy_defuzzify_cog(values, grades):
    dx = values[1] - values[0]
    area = sum([grades[i] * dx for i in range(len(values))])
    x = sum([values[i] * grades[i] * dx for i in range(len(values))])
    y = sum([grades[i] * grades[i] * dx for i in range(len(values))])
    return [x / area, 0.5 * (y / area)]
