from math import cos, tan
try:
    x = float(input("x="))
    y = float(input("y="))
    res = (1 - tan(x)) ** (1 / tan(x)) + cos(x-y)
    print("Result:", res)
except ValueError:
    print("ERROR!!! you should enter a number but not string!!!")