from math import tan, cos
while (True):
    try:
        x=float(input("Enter x ="))
        if (x==0):
            raise ValueError
        break
    except ValueError:
        print("Wrong data type of x(must be real number, except 0)")
while (True):
    try:
        y=float(input("Enter y ="))
        break
    except ValueError:
        print("Wrong data type of y")

print("Result = {}".format(pow(1-tan(x),1/tan(x))+cos(x-y)))