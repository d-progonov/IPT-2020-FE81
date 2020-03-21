try:
    x = float(input("Enter first number"))
    y = float(input("Enter second number"))
    if x < 0 or y < 0:
        print("ERROR!!!! You should enter not negative number number")
    else:
        def A(n, m):
            if n == 0:
                return m + 1
            if n != 0 and m == 0:
                return A(n-1, 1)
            if n > 0 and m > 0:
                return A(n - 1, A(n, m - 1))
        print("Result of Ackerman function is: ", A(x, y))

except ValueError:
    print("ERROR!!! you should enter a number but not string!!!")
