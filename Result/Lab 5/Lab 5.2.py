try:
    
    n = float(input("Enter n = "))
    x = float(input("Enter x = "))

    def rec(n):
        if n==0:
            return 1
        elif n < 0:
            return (x ** n) + rec(n+1)
        else:
            return (x ** n) + rec(n-1)
    print (rec(n))
except ValueError:
    print("You entered the wrong type")
