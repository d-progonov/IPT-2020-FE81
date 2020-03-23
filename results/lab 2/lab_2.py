import math

while(True):
    try:
        a = float(input("Enter number A here: "))
        break
    except ValueError:
        print("No, you entered wrong data! Try again!")

while(True):
    try:
        b = float(input("Enter number B here: "))
        break
    except ValueError:
        print("No, you entered wrong data! Try again!")

while(True):
    try:
        c = float(input("Enter number C here: "))
        break
    except ValueError:
        print("No, you entered wrong data! Try again!")

if b >= a <= c:
    print("Min of these 3 numbers is: ", a, "\nThank you!")
elif a  >= b <= c:
    print("Min of these 3 numbers is: ", b, "\nThank you!")
else :
    print("Min of these 3 numbers is: ", c, "\nThank you!")



