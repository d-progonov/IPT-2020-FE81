while (True):
    try:
        a=float(input("Enter the first number ="))
        break
    except ValueError:
        print("Wrong data type of the first number")
while (True):
    try:
        b=float(input("Enter the second number ="))
        break
    except ValueError:
        print("Wrong data type of the second number")
while (True):
    try:
        c=float(input("Enter the third number ="))
        break
    except ValueError:
        print("Wrong data type of the third number")
if (a==b) or (b==c) or (a==c):
    a+=5
    b+=5
    c+=5
    print("The first = {0}, the second = {1},the third = {2}".format(a,b,c))
else: print("There aren`t equal numbers")