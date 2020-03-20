try:
    a = float(input("Enter your a number"))
    if a == 0:
        print("We can't divide by 0")
    else:
        b = float(input("Enter your b number"))
        f = float(input("Enter your f number"))
        res = ((a + b - f) / a) + f * a ** 2 - (a + b)
        print(res)
except ValueError:
    print("ERROR you should enter a number but not string!!!")