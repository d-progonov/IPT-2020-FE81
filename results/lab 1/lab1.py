try:
    x = float(input("Enter x : "))
    y = float(input("Enter y : "))
    if x != y and x >= 0:
        res = (1/(x**3-y**3))-((2*x)**(1/2))
        print("Your result :", round(res, 3))
    else:
        print("Error x cannot be negative or equal to y\n")
except ValueError:
    print("You entered the wrong type")
