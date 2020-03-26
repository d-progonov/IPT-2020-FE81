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
 
# B-part
'''
Рекурсія: знайти суму n членів арифметичної прогресії із заданим початковим членом та кроком.
'''

def sumAr(f, s, endpos):
    if (endpos == 1):
        return s
    return f + (endpos-1) * s + sumAr(f, s,endpos-1)

try:
    n = abs(int(input("Enter n: ")))
    
    first = int(input("Enter first element: "))
    step = int(input("Enter step: "))

    print(sumAr(first, step, n))

except ValueError:
    print("Error: values must be numeric.")
