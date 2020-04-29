'''
 * File: Lab10.py
 * Project: Python Labs
 * Variant: 20
 * Created Date: 29.04.20
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 

Example of Data:
HEX|   1 |  2  |  3  |  4  |  5   |  6	 |   7	|    8   |   9   |  10   |  11   |  12   |   13   |
FIB|   1 |  10 | 100 | 101 | 1000 | 1001 | 1010 |  10000 | 10001 | 10010 | 10100 | 10101 | 100000 |
'''
# Class of user's errors, based on Exception class
class MyException(Exception):
    def init(self, text):
        self.txt = text

def fibbGen(n):
    f0 = 0; f1 = 1;     # edge elements
    resnum = []         # an array of fibonacci numbers, that form the original number 
    num = -1            # counter for index 
    finalRes = ''            # final result
    
    while (not(n == 0)): 
        while (f1 <= n):            # until find the number, which higher than original
            f0, f1 = f1, f0 + f1;   # swap edge elem
            num = num + 1 
            if (f1 > n):            # if curr endge elem higher than original
                n = n - f0          # we delete it
                resnum.append(num)  # and add to list
                f0, f1 = 0, 1;      # reset edge numbers 
                num = -1            # and counter
    i = resnum[0]   # at that moment we have list of indexes of fib numbers
    
    while (i > 0):  # processing that list 
        k = 0; check = False; 

        while (k < len(resnum)): 
            if (i == resnum[k]):
                finalRes = finalRes + '1'
                check = True
            k = k + 1
        
        if (check == False):
            finalRes = finalRes + '0'
        i = i - 1
    return finalRes

try:
    A = int(input("Enter non-negative integer number: " ))
    newA = fibbGen(A)
    print("Your new A is: ", newA)
    if A < 0:
      raise MyException("A must be non-negative!")

except ValueError:
    print("Wrong input data.")
    
except MyException as nonNegative:
    print(nonNegative)
