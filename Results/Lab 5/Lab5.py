import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from include.usefullFuncs import check_input_data


def g(a, c, n):
    return (a*(n + c)) % 10


def f(a, m, c=1):
    if m <= 9:
        if m >= 0:
            return m
    return g(a, c, m) * f(a, (m - 1 - g(a, m, c)), c) + m


def lab5_1():
    print("HI! Lab5!")
    a = input("Input a: ")
    m = input("Input m: ")
    c = input("Input c: ")

    a = check_input_data(1, a)
    c = check_input_data(1, c)
    m = check_input_data(1, m)

    return f(a, m, c)

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

def lab5_2():
    print("HI! Lab5!")
    a = input("Input a: ")
    a = check_input_data(1, a)
    fibon(a)

print(lab5_1())
lab5_2()
