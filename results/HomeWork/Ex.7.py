try:
    x = int(input("Enter your 2-digital number"))
    if x <= 0:
        print("ERROR!!! you should enter natural number")
    elif 9 < x < 100:
        x = list(str(x))
        print("min=", min(x), "max=", max(x))
    else:
        print("ERROR!!! Enter your 2-digital number")
except ValueError:
    print("ERROR!!! you should enter a number but not string!!!")