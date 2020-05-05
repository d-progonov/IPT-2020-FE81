import sys, os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from include.usefullFuncs import check_input_data

import matplotlib.pyplot as plt
import numpy as np


def get_x(t, a):
    x = []
    size = len(t)
    for i in range(0, size, 1):
        x.append((a * (t[i] ** 2)) / (1 + (t[i] ** 2)))
    return x


def get_y(t, a):
    y = []
    size = len(t)
    for i in range(0, size, 1):
        y.append((a * (t[i] ** 3)) / (1 + (t[i] ** 2)))
    return y


def lab8():
    print("HI! Lab8!")
    a = input("Input a: ")
    a = check_input_data(1.1, a)

    tMin = input("Input min t value: ")
    tMin = check_input_data(1.1, tMin)
    if tMin == False:
        return "wrong t input"

    tMax = input("Input max t value: ")
    tMax = check_input_data(1.1, tMax)
    if tMax == False:
        return "wrong t input"

    if a <= 0.0:
        return "a must be greater than 0"

    if tMax < tMin:
        return "wrong tMax"

    t = np.arange(tMin, tMax, 0.1)

    x = get_x(t, a)
    y = get_y(t, a)

    plt.plot(x, y, 'r--')
    plt.show()


print(lab8())
