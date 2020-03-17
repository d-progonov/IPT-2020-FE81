try:
    x = float(input("Enter your number: "))
    print("Enter 1 for calculating your number squared")
    print("Enter 2 to calculate  your number cubed")
    print("and etc")
    res = int(input())
    x = x ** (res+1)
    print(x)
except ValueError:
    print("ERROR you should enter a number but not string!!!")
