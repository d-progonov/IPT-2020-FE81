'''
 * File: Lab5.py
 * Project: Python Labs
 * Variant: 20
 * Created Date: 28.03.20
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 
 '''

# A-part

def p(x, arr):
    for elem in arr:
        elem = elem*(x**i) 
    return sum(arr)

try:
    A = []
    s = float(input("Ented s: "))
    t = float(input("Ented t: "))
    print("Add elem to a0...a12: ")

    for i in range (1, 14):
        elem = float(input())
        A.append(elem)
    
    res = p(1,A) - p(t, A) + (p(s-t, A))**2 - p(1, A)**3 
    print("Result is:", res)

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
