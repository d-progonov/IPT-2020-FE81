try:
    
    n = float(input("Enter n = "))
    x = float(input("Enter x = "))

    def fonc(n,x):
        if n==0:
            return 1
        elif n < 0:
            return (x ** n) + fonc(n+1,x)
        else:
            return (x ** n) + fonc(n-1,x)
    print (fonc(n,x))
except ValueError:
    print("You entered the wrong type")
