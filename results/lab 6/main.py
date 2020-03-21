import functions
try:
    m = int(input("Enter first number NSD"))
    n = int(input("Enter second number NSD"))
    if m <= 0 or n <= 0:
        print("ERROR!!!! You should enter natural number")
    else:
        print("NSD=", functions.nsd(m, n))

    x = float(input("Enter first number Ackerman arg"))
    y = float(input("Enter second number Ackerman arg"))
    if x < 0 or y < 0:
        print("ERROR!!!! You should enter not negative number number")
    else:
        print("Result of Ackerman function is: ", functions.A(x, y))
except ValueError:
    print("ERROR!!! you should enter a number but not string!!!")