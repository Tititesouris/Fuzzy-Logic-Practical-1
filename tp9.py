import matplotlib.pyplot as plt
from matplotlib.colors import *
from fuzzylogic import *


def low_temp(temperature):
    return fuzzy_trapezoid(0, 0, 10, 20, temperature)


def medium_temp(temperature):
    return fuzzy_trapezoid(10, 20, 20, 30, temperature)


def high_temp(temperature):
    return fuzzy_trapezoid(20, 30, 40, 40, temperature)


membership_functions = [low_temp, medium_temp, high_temp]
colors = [
    to_rgb("blue"),
    to_rgb("orange"),
    to_rgb("red")
]
xMin, xMax, xStep = 0, 40, 0.01


def show_membership_functions():
    plt.title("Temperature membership functions")
    x_data = np.arange(xMin, xMax, xStep)
    for i, membership_function in enumerate(membership_functions):
        y_data = np.array(list(map(membership_function, x_data)))
        plt.plot(x_data, y_data, color=colors[i])
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
    plt.plot(x_data, y_data, color=np.interp((0.5, 0.5, 0.5), colors[0], colors[1]))
    plt.show()


def show_not_low_and_high_temp():
    plt.title("Not (low and high) temperature membership function")
    x_data = np.arange(xMin, xMax, xStep)
    not_low_and_high_temp = [
        fuzzy_not,
        [
            fuzzy_and,
            [low_temp],
            [high_temp]
        ]
    ]
    y_data = fuzzy_combine(not_low_and_high_temp, x_data)
    plt.plot(x_data, y_data, color=np.interp((0.5, 0.5, 0.5), colors[0], colors[2]))
    plt.show()



show_membership_functions()
print(fuzzy_grades(membership_functions, 16))
show_low_or_medium_temp()
show_not_low_and_high_temp()
