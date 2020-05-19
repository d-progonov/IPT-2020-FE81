# Lab 1
# Var 21

import math

def func():
    try:
        x = float(input("Enter X value: "))
        z = float(input("Enter Z value: "))
        y = math.log((math.fabs(z - math.sqrt(math.fabs(x)))), 4) 
        print("Result:", y)

    except ValueError:
        print("\n", "Error: wrong input data.")

func()
