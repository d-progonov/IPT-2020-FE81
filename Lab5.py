'''
 * File: Lab5.py
 * Project: Python Labs
 * Variant: 20
 * Created Date: 28/03/2020
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: 01/04/2020
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 
 '''

# A-part

def p(x, Ar):
    sum1 = 0
    for i in range(0, 13):
        elem = (Ar[i])*x**i
        sum1 += elem
    return sum1

def polinome(A, s, t):
    pol = p(1, A) - p(t, A) + (p(s-t, A))**2 - (p(1, A))**3 
    print("Result of polinome is:", pol)

try:
    s1 = float(input("Enter s: "))
    t1 = float(input("Enter t: "))
    
    print("Enter elements from a0 to a12: ")
    A1 = [float(input("current element: ")) for i in range(0, 13)]

    polinome(A1, s1, t1)
    
except ValueError:
    print("Error: values must be numeric.")


# B-part (4)

def gcd(a, b):
  if b == 0: 
      return a
  else:
      r = a % b
      return gcd(b, r)

try:
    n = abs(int(input("Enter n: ")))
    m = abs(int(input("Enter m: ")))

    print("GCD is: ", gcd(m, n))

except ValueError:
    print("Error: values must be numeric.")
