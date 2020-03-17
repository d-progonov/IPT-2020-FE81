'''
 * File: Lab3.py
 * Project: Python Labs
 * Variant: 20
 * Created Date: 18.03.20
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 
 '''


# If we want to get result in [0, inf):
'''
from mpmath import nsum, inf

def zetoToinf():
    s = nsum(lambda i: (1 / (pow(2, i) ) + (1 / (pow(3, i)))), [0, inf])
    print(s)
zetoToinf()
'''


# If we want to get result in [0, N]:
N = int(input("Number of elements: "))
sum = 0
i = 0
while i < N:
    elem = (1 / (pow(2, i) ) + (1 / (pow(3, i))))
    print(i,"- element is: ", elem)
    sum = sum + elem
    i = i + 1
print(float("{0:.4f}".format(sum)))

'''
Пояснення:
    У першому випадку, використовуючи модуль mpmath для точних обчислень на мові Python,
    та вбудованної функції nsum. lambda-запис дозволяє автоматично повертати та відразу 
    записувати результат у функцію nsum. Такий специфічний запис забезпечує вміщення логіки
    всього лише в один рядок коду.

    Результатом виконання функції zetoToinf() є число 3.5 (3.5001).

    У другому випадку, використовуючи вбудовані в мову Python цикли while або for, 
    досягається отримання суми ітеративним шляхом. На відмінно від першого прикладу, 
    користувач може задати N-число, тобто кінцеве. Сума проходить формат {0:.4f}, 
    тобто дотримується умови: е = 10^-4.

    Результатом виконання программи є число 3.5 (починаючи з числа i=16).

    Тож можна зробити висновок про те, що ряд - збіжний.
'''
