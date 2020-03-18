from math import cos, tan

print("(1-tg x)^(ctg x)+cos(x-y)")
while(1):
    try:
        x = float (input("Enter x = "))
        1/tan(x)
        break
    except ValueError:
        print("Wrong data type for variable x (must be float).")
    except ZeroDivisionError:
        print("Division by zero (ctg(x)=cos(x)/sin(x) <- sin(0)=0)")
while(1):
    try:
        y = float (input("Enter y = "))
        break
    except ValueError:
        print("Wrong data type for variable y (must be float).")

print("(1-tg x)^(ctg x)+cos(x-y) =", (pow(1-tan(x),1/tan(x))+cos(x-y)))
input("Any key to exit...")