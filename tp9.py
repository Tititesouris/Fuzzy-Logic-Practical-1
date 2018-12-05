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
names = ["Low", "Medium", "High"]
colors = [
    to_rgb("blue"),
    to_rgb("orange"),
    to_rgb("red"),
    to_rgb("gold"),
    to_rgb("purple"),
    to_rgb("green")
]
x_min, x_max, x_step = 0, 40, 0.01
x_min_heat, x_max_heat, x_step_heat = 0, 15, 0.01


def show_membership_functions():
    plt.title("Temperature membership functions")
    x_data = np.arange(x_min, x_max, x_step)
    for i, membership_function in enumerate(membership_functions):
        y_data = list(map(membership_function, x_data))
        plt.plot(x_data, y_data, color=colors[i], label=names[i])
    plt.ylim((-0.1, 1.1))
    plt.xlabel("Temperature (°C)")
    plt.legend()
    plt.show()


def show_low_or_medium_temp():
    plt.title("Low or medium temperature membership function")
    x_data = np.arange(x_min, x_max, x_step)
    low_or_medium_temp = [
        fuzzy_or,
        [low_temp],
        [medium_temp]
    ]
    y_data = fuzzy_combine(low_or_medium_temp, x_data)
    plt.plot(x_data, y_data, color=colors[3])
    plt.ylim((-0.1, 1.1))
    plt.xlabel("Temperature (°C)")
    plt.show()


def show_not_low_and_medium_or_medium_and_high_temp():
    plt.title("Not ((low and medium) or (medium and high)) temperature membership function")
    x_data = np.arange(x_min, x_max, x_step)
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
    plt.xlabel("Temperature (°C)")
    plt.show()


def show_fuzzy_implication(temperature):
    plt.subplot(1, 2, 2)
    plt.title("Fuzzy implication for temperature of " + str(temperature) + "°C")
    x_data = np.arange(x_min_heat, x_max_heat, x_step_heat)
    y_data = list(map(heat, x_data))
    plt.plot(x_data, y_data, color=colors[5], linestyle=":", linewidth=1)
    y_data = fuzzy_imply_mamdani(low_temp(temperature), heat, x_data)
    plt.plot(x_data, y_data, color=colors[5])
    center_of_gravity = fuzzy_defuzzify_cog(x_data, y_data)
    plt.plot(center_of_gravity[0], center_of_gravity[1], "ro", label="Center of gravity")
    plt.ylim((-0.1, 1.1))
    plt.xlabel("Heating power (kW)")
    plt.legend()

    plt.subplot(1, 2, 1)
    plt.title("Low temperature membership function")
    x_data = np.arange(x_min, x_max, x_step)
    y_data = list(map(low_temp, x_data))
    plt.plot(x_data, y_data, color=colors[0])
    plt.vlines(temperature, ymin=0, ymax=low_temp(temperature), color="red", linestyle="--", linewidth=1)
    plt.hlines(low_temp(temperature), xmin=temperature, xmax=73, color="red", linestyle="--", linewidth=1,
               clip_on=False)
    plt.xlim((x_min, x_max))
    plt.ylim((-0.1, 1.1))
    plt.xlabel("Temperature (°C)")
    plt.show()


show_membership_functions()
print(fuzzy_grades(membership_functions, 16))
show_low_or_medium_temp()
show_not_low_and_medium_or_medium_and_high_temp()
show_fuzzy_implication(12)
