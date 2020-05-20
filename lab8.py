from math import isinf,isnan
import numpy as np
import matplotlib.pyplot as plt

def func (x):
    try:
        return 1/(3*pow(x,2)+2*x+1)
    except ZeroDivisionError:
        print("Error; divided by zero")

def coef():
    while 1:
        try:
            max=int(input("Enter max point of graph: "))
        except ValueError:
            print("Error; enter integer number")
            continue
        if isnan(max):
            print("Error; Is not a number")
            continue
        if isinf(max):
            print("Error; Is an infinity")
            continue
        try:
            min=int(input("Enter min point of graph: "))
        except ValueError:
            print("Error; enter integer number")
            continue
        if isnan(max):
            print("Error; Is not a number")
            continue
        if isinf(max):
            print("Error; Is an infinity")
            continue
        try:
            dx=float(input("Enter a step: "))
        except ValueError:
            print("Error; enter integer number")
            continue
        if isnan(max):
            print("Error; Is not a number")
            continue
        if isinf(max):
            print("Error; Is an infinity")
            continue
        if max<min:
            print("Error; Maximum is smaller than minimum")
            continue
        else:
            break
    coef=[max,min,dx]
    return coef

if __name__ == "__main__":
    coef=coef()
    xlist = np.arange (coef[1], coef[0], coef[2])
    ylist = [func (x) for x in xlist]
    plt.plot (xlist, ylist)
    plt.show()

