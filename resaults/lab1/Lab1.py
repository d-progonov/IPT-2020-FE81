from math import log
 
x = input('Input x = ')
a = input('Input a = ')

while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        x = input("Enter an integer number x = ")

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        a = input("Enter an integer number a = ")
        
if a != 0:
    a == a
else:
    a = int(input("Enter a number a!=0. a = "))
    
if x > 0 and a > 0:
   x == x and a == a
elif x < 0 and a < 0:
    x == x and a == a
else:
    x = int(input("Enter a number with signum like a and x!=0. x = ")) 

def sign(x,a):
    if (x - 2*a) > 0:
        return 1
    elif (x - 2*a) == 0:
        return 0
    else:
        return -1

y = sign(x,a) + log(x/a, 3)
print('y =', y)
