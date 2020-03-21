import sys, os, math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from include.usefullFuncs import check_input_data


def lab1():
    print("HI! Lab1!")
    x = input("Input x: ")
    b = input("Input b: ")

    result = check_input_data(1.1, x)
    if result:
        x = result
    else:
        return "WRONG INPUT"

    print("x = ", x)
    result = check_input_data(1.1, b)
    if result:
        b = result
    else:
        return "WRONG INPUT"

    print("b = ", b)

    if x % 90 == 0:
        if x % 180 != 0 & x % 360 == 0:
            return "x is OUT of range"
    if b == 0:
        return "b is OUT of range"
    if x - b < 0:
        return "b or x is OUT of range"

    return ((math.sqrt(x - b)) / (2 * b)) - (math.tan(math.radians(x)) / (b * b))


print(lab1())
