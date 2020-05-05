import sys, os

import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from include.usefullFuncs import check_input_data


def g(a, c, n):
    return (a * (n + c)) % 10


def f(a, m, c=1):
    if m <= 9:
        if m >= 0:
            return m
    return g(a, c, m) * f(a, (m - 1 - g(a, m, c)), c) + m


def fibon(n):
    if n < 0:
        print("wrong input")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    return fibon(n - 1) + fibon(n - 2)


def lab6():
    print("HI! Lab6!")

    with open("data.txt", "r") as read_file:
        data = json.load(read_file)

    a = check_input_data(1, data["a Param"])
    c = check_input_data(1, data["c Param"])
    m = check_input_data(1, data["m Param"])
    fibNum = check_input_data(1, data["fibNum"])

    out = open("output.txt", "w")
    print(f(a, m, c))
    out.write("f(m)= " + str(f(a, m, c)) + "\n")
    out.write("fibon(fibNum)= " + str(fibon(fibNum)))
    out.close()


lab6()