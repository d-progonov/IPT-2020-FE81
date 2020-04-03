from math import sin
while (True):
    try:
        s=float(input("Enter s="))
        break
    except ValueError:
        print("Wrong data type of s")
while (True):
    try:
        t=float(input("Enter t="))
        break
    except ValueError:
        print("Wrong data type of t")

def f(a, b, c):
    return (2*a-b-sin(c))/(5+abs(c))

print("Result={:.4f}".format(f(t, -2*s, 1.17)-f(2.2, t, s-t)))