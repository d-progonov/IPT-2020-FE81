import math

try:
    print("Enter 1 for calculating cosinus of your number ")
    print("Enter 2 to calculate sinus of your number")
    print("Enter 3 to calculate tangens of your number")
    res = float(input("Enter number from 1 to 3: "))
    x = int(input("Enter your number: "))
    if res == 1:
        x = math.cos(x)
        print(x)
    if res == 2:
        x = math.sin(x)
        print(x)
    if res == 3:
        x = math.tan(x)
        print(x)
    
except ValueError:
    print("ERROR you should enter a number!!!")
