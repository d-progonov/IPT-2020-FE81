while (True):
    try:
        a=float(input("Enter a="))
        break
    except ValueError:
        print("Wrong data type of a")
while (True):
    try:
        b=float(input("Enter b="))
        break
    except ValueError:
        print("Wrong data type of b")
while (True):
    try:
        c=float(input("Enter c="))
        break
    except ValueError:
        print("Wrong data type of c")
if b>= a <= c:
    print("Min of (a,b,c) is a={}".format(a))
elif c>= b <=a:
    print("Min of (a,b,c) is b={}".format(b))
else:
    print("Min of (a,b,c) is c={}".format(c))
