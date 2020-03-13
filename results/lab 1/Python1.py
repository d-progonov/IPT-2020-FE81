from math import exp, log
 
x = input('x = ')

while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        x = input("Enter a number greater than four. x = ")

while x <= 4:
    try:
        x = int(input("Enter a number greater than four. x = "))
    except ValueError:
        x = input("Enter a number. x = ")

a = input('a = ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        a = input("Enter a number. a = ")
 
y = log(x-4, 2) + exp(2*a-x)
print('y =', y)