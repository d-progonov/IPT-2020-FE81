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
        f=float(input("Enter f="))
        break
    except ValueError:
        print("Wrong data type of f")

print("Result={}".format((a+b-(f/a))+(f*a*a)-(a+b)))