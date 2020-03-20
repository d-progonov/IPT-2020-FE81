try:
    n = float(input("Enter your n number"))
    k = float(input("Enter your power number"))
    i=1
    res=1
    while i <= k:
        res *=n
        i += 1
    print(res)
except ValueError:
    print("ERROR!!! you should enter a number but not string!!!")