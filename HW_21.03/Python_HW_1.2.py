while(1):
    try:
        a = float (input("Enter a = "))
        1/a
        break
    except ValueError:
        print("Wrong data type for variable a (must be float).")
    except ZeroDivisionError:
        print("Denominator must not be equal to 0. 1/a")
while(1):
    try:
        b = float (input("Enter b = "))
        break
    except ValueError:
        print("Wrong data type for variable b (must be float).")
while(1):
    try:
        f = float (input("Enter f = "))
        break
    except ValueError:
        print("Wrong data type for variable f (must be float).")

print("(а + b — f / а) + f * a * a — (a + b) = ", ((a+b-f/a)+f*a*a-(a+b)))
input("Any key to exit...")