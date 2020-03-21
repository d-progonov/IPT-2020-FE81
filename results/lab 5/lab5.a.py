try:
    m = int(input("Enter first number"))
    n = int(input("Enter second number"))
    if m <= 0 or n <= 0:
        print("ERROR!!!! You should enter natural number")
    else:
        def nsd(m , n):
            if n == 0:
                return m
            else:
                return nsd(n, m % n)
        print("NSD=", nsd(m, n))
except ValueError:
    print("ERROR!!! you should enter a number but not string!!!")
