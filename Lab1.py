'''
 * File: Lab1.py
 * Project: Python Labs
 * Variant: 20
 * Created Date: 12.02.20
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 
 '''

# Кequired modules:
import math as mt
import numpy as np

# Processing input data:
def func():
    try:
        x = float(input("Enter X value: "))
        z = float(input("Enter Z value: "))
        y = z + (x / (z**2 - mt.fabs(x**2 / (z - (x**3) / 3) ) ) )
    
        print("Result  is:", y)

    except ValueError:
        print("\n", "Error: invalid input value.")
        print(" Data must be numeric (floating-point)!")
    
    except ZeroDivisionError:
        print("\n", "Error: zero division!")
        print(" Denominator must be non-zero!")

# Call:
func()
