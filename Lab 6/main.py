'''
 * File: Lab1.py
 * Project: Python Labs
 * Variant: 20
 * Created Date: 02.04.20
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 
 '''

import functions as func

try:
    s1 = float(input("Enter s: "))
    t1 = float(input("Enter t: "))
    
    print("Enter elements from a0 to a12: ")
    A1 = [float(input("current element: ")) for i in range(0, 13)]

    func.polinome(A1, s1, t1)

    n = abs(int(input("Enter n: ")))
    m = abs(int(input("Enter m: ")))

    print("GCD is: ", func.gcd(m, n))

except ValueError:
    print("Error: values must be numeric.")