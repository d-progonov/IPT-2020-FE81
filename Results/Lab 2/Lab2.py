import sys, os, math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from include.usefullFuncs import check_input_data


def lab2():
    print("HI! Lab2!")
    x = input("Input x: ")

    result = check_input_data(1.1, x)
    if result:
        x = result
    else:
        return "WRONG INPUT"

    print("x =", x)

    if x < 0:
        x = pow(x, 2)
    elif x > 0:
        x = 3*x

    return x

print(lab2())