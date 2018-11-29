import matplotlib.pyplot as plt
from matplotlib.colors import *
from fuzzylogic import *


def low_temp(temperature):
    return fuzzy_trapezoid(0, 0, 10, 20, temperature)


def medium_temp(temperature):
    return fuzzy_trapezoid(10, 20, 20, 30, temperature)


def high_temp(temperature):
    return fuzzy_trapezoid(20, 30, 40, 40, temperature)


def heat(kW):
    return fuzzy_trapezoid(8, 10, 15, 15, kW)


membership_functions = [low_temp, medium_temp, high_temp]
colors = [
    to_rgb("blue"),
    to_rgb("orange"),
    to_rgb("red"),
    to_rgb("yellow"),
    to_rgb("purple"),
    to_rgb("green")
]
xMin, xMax, xStep = 0, 40, 0.01
xMinHeat, xMaxHeat, xStepHeat = 0, 15, 0.01


def show_membership_functions():
    plt.title("Temperature membership functions")
    x_data = np.arange(xMin, xMax, xStep)
    for i, membership_function in enumerate(membership_functions):
        y_data = np.array(list(map(membership_function, x_data)))
        plt.plot(x_data, y_data, color=colors[i])
    plt.ylim((-0.1, 1.1))
    plt.show()


def show_low_or_medium_temp():
    plt.title("Low or medium temperature membership function")
    x_data = np.arange(xMin, xMax, xStep)
    low_or_medium_temp = [
        fuzzy_or,
        [low_temp],
        [medium_temp]
    ]
    y_data = fuzzy_combine(low_or_medium_temp, x_data)
    plt.plot(x_data, y_data, color=colors[3])
    plt.ylim((-0.1, 1.1))
    plt.show()


def show_not_low_and_medium_or_medium_and_high_temp():
    plt.title("Not ((low and medium) or (medium and high)) temperature membership function")
    x_data = np.arange(xMin, xMax, xStep)
    not_low_and_medium_or_medium_and_high_temp = [
        fuzzy_not,
        [
            fuzzy_or,
            [
                fuzzy_and,
                [low_temp],
                [medium_temp]
            ],
            [
                fuzzy_and,
                [medium_temp],
                [high_temp]
            ]
        ]
    ]
    y_data = fuzzy_combine(not_low_and_medium_or_medium_and_high_temp, x_data)
    plt.plot(x_data, y_data, color=colors[4])
    plt.ylim((-0.1, 1.1))
    plt.show()


def show_fuzzy_implication(temperature):
    plt.title("Fuzzy implication for temperature of " + str(temperature) + "°C")
    x_data = np.arange(xMinHeat, xMaxHeat, xStepHeat)
    all_temp = fuzzy_or(low_temp(temperature), fuzzy_or(medium_temp(temperature), high_temp(temperature)))
    y_data = fuzzy_imply(all_temp, heat, x_data)
    plt.plot(x_data, y_data, color=colors[5])
    plt.ylim((-0.1, 1.1))
    plt.show()


# show_membership_functions()
print(fuzzy_grades(membership_functions, 16))
# show_low_or_medium_temp()
# show_not_low_and_medium_or_medium_and_high_temp()
show_fuzzy_implication(12)
