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

if a>b:
    print("Greater than second one")
elif a<b:
    print("Less than second one")
else: print("These numbers are equal")