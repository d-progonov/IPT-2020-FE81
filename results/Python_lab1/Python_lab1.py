from math import cos

while(1):
    try:
        a = float (input("Enter a = "))
        1/(a+2)
        break
    except ValueError:
        print("Wrong data type for variable a (must be float).")
    except ZeroDivisionError:
        print("Denominator must not be equal to 0. 1/(a+2)")
while(1):
    try:
        x = float (input("Enter x = "))
        1/(x-1)
        break
    except ValueError:
        print("Wrong data type for variable x (must be float).")
    except ZeroDivisionError:
        print("Denominator must not be equal to 0. 1/(x-1)")

y = ((x**3)+(2*a*x)+3)/((x-1)**2)+cos(x**2)/(a+2)
print("result y = ", round(y,3))
input("Any key to exit...")
