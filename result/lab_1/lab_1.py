from math import exp, log
class LogError(Exception):
    pass

while (True):
    try:
        x=float(input("Enter x="))
        if x<=4:
            raise LogError
        break
    except ValueError:
        print("Wrong data type of x")
    except LogError:
        print("Logarithm of negative number")

while (True):
    try:
        a=float(input("Enter a="))
        break
    except ValueError:
        print("Wrong data type of a")

y=log(x-4,2)+exp(2*a-x)

print("Result: y={}".format(round(y,4)))
