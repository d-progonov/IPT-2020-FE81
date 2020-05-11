def fastPow(x, n):
    def even(n):
        if n % 2 == 0:
            return True
        return False
    if n==0:
        return 1
    if even(n):
        return fastPow(x, n/2)**2
    return x*fastPow(x, n-1)

def main():
    a = int(input("Enter your value: "))
    b = input("Enter your power value: ")
    negat = False
    b1 = 0
    b2 = 0
    
    try:
        b = int(b)
        if b < 0:
            negat = True
            b = abs(b)
    except ValueError: print("The degree of the number cannot be converted to integers")

    if type(b) == str:
        b = float(b)
        if b < 0:
            negat = True
            b = abs(b)
        b1 = int(b // 1)
        b2 = b % 1

    try:
        if b1 == 0 and b2 == 0:
            if negat:
                answ = 1 / fastPow(a, b)
            else:
                answ = fastPow(a, b)
            print("Resault is: ", answ)
        else:
            answ1 = fastPow(a, b1)
            answ2 = pow(a, b2)
            if negat:
                answ = 1 / (answ1 * answ2)
            else:
                answ = answ1 * answ2
            print("Resault is: ", answ)
    except OverflowError: print("The answer is too big")

main()
