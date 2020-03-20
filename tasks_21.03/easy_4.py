while (True):
    try:
        x=float(input("Enter x ="))
        break
    except ValueError:
        print("Wrong data type of x)")
while (True):
    try:
        y=float(input("Enter y ="))
        break
    except ValueError:
        print("Wrong data type of y)")
while (True):
    try:
        z=float(input("Enter z ="))
        break
    except ValueError:
        print("Wrong data type of z)")

print("Result = {}".format(pow(pow(x,2)+pow(y,2)+pow(z,2),0.5)))