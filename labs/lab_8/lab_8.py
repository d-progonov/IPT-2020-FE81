import matplotlib.pyplot as plt
from numpy import arange
import numpy as np



def in_data():
    try:
        a = float(input("Please, input first koeficient(a): "))
        b = float(input("Please, input second koeficient(b): "))
        xmin = float(input("Please, input left limit for x: "))
        xmax = float(input("Please, input right limit for x: "))
        stp = float(input("Please, input a step of graphic(stp): "))

        if stp < 0.00001:
            raise Exception

        return a, b, xmin, xmax, stp

    except ValueError:
        e = input("You have to enter only numeric data.\nIf you want to break this program, please enter \"e\": ")
        if (e.lower() == "e"):
            raise SystemExit(0)
        in_data()
    except Exception:
        print("The step must be bigger then 0.00001")
        in_data()

def func(a, b, x):
    return (b - 2/(a*x - b) - 3/(x**2 - b))

def main():
    xlist = list()
    a, b, xmin, xmax, stp = in_data()
    x_zer = [b/a, -np.sqrt(b), np.sqrt(b)]
    print(x_zer)
    for i in arange(xmin, xmax + stp, stp):
        xlist.append(i)
        if i in x_zer:
            xlist[-1] = np.nan
    ylist = [func(a, b, x) for x in xlist]
    plt.plot(xlist, ylist)
    plt.minorticks_on()
    plt.grid(which='major', linestyle = '--')
    plt.grid(which='minor', linestyle = ':')
    plt.show()

if __name__ == "__main__":
    main()

