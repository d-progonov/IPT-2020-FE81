try:
    k = float(input("Enter your k number"))
    n = float(input("Enter your n number"))
    i = 1
    res = 0
    while i <= n:
        res += i ** k
        i += 1
    print(res)
except ValueError:
    print("ERROR you should enter a number but not string!!!")