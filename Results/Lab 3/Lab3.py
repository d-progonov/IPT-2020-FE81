import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from include.usefullFuncs import check_input_data



def a(n):
    return n / pow((n - 1), 2)


def lab3_1():
    print("HI! Lab3.1!")
    E = pow(10, -4)
    a_sum = 0.0
    n = 2
    while True:
        curr = a(n)
        if curr <= E:
            break
        a_sum += curr
        n += 1

    return a_sum


def lab3_2():
    print("HI! Lab3.2!")
    n = check_input_data(1, input("Input n: "))
    firstElem = check_input_data(1, input("Input first element: "))

    if firstElem < 0 or n < 0:
        return "Wrong input"

    counter = 0
    for i in range(firstElem, firstElem+n+1, 1):
        if ((i - firstElem + 1) % 2) == 0:
            if not (i % 2) == 0:
                counter += 1
    return ("There are " + str(counter) + " elems")


print(lab3_1())
print(lab3_2())
