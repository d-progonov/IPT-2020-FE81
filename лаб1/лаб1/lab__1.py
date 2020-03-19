import math


def funct(x, a):
    print(math.log(x ** 3) + 1 / math.sin(a))


while True:
    try:
        X = input("x = ")
        x = float(X)
        if  x <= 2:
            print("error.enter x > 2")
        else:
            if math.isnan(x):
             print("enter x")
            else:
                if math.isinf(x):
                 print("enter x")
                else:
                    break
    except ValueError:
        print("Is not a number! Try again!")

while True:
    try:
        A = input("a = ")
        a = float(A)
        if  a == 0:
            print("error.enter a != 0")
        else:
            if math.isnan(a):
                print("enter a")
            else:
                if math.isinf(a):
                    print("enter a")
                else:
                    break
    except ValueError:
        print("Is not a number! Try again!")

funct(x, a)
from time import *
sleep(10000)

