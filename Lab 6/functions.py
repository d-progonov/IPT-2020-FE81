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

# B-part (4)

def gcd(a, b):
  if b == 0: 
      return a
  else:
      r = a % b
      return gcd(b, r)