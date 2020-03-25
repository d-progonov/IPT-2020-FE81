import math

try:
    x = float(input("Enter x : "))
    y = float(input("Enter y : "))
    if x != y and x >= y and x >= 0:
        res = (((x**3)-(y**3))**(1/2))+(math.log10(x+5))
        print("Your result :", round(res, 3))
    else:
        print("Error x cannot be negative or equal or less to y\n")
except ValueError:
    print("You entered the wrong type")
