'''
 * File: Lab4.A.py
 * Project: Python Labs
 * Variant: 20
 * Created Date: 20.03.20
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 
 '''

# A-part (done):

import numpy as np
np.set_printoptions(precision=3)

def factorial(i):
    if i == 0:
        return 1
    return factorial(i-1) * i

A = int(input("Enter matrix order: " ))
Arr = [[ (1 / (factorial(j))**i) for i in range(1, A+1)] for j in range(1, A+1)] 
Arr = np.transpose(Arr)

for A in Arr: 
    print(A)
