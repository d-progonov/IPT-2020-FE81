try:
    x = float(input("Enter your number: "))
    print("Enter 1 for calculating your number squared")
    print("Enter 2 to calculate  your number cubed")
    res = int(input())
    if res == 1:
        x = x ** 2
        print(x)
    elif res == 2:
        x = x ** 3
        print(x)
    else:
        print("ERROR you should enter 1 or 2")
except ValueError:
    print("ERROR you should enter a number but not string!!!")