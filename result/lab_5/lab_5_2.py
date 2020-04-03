while (True):
    try:
        b = float (input("Enter b1="))
        break
    except ValueError:
        print("Wrong data type of b1")
while (True):
    try:
        q = float (input("Enter step="))
        break
    except ValueError:
        print("Wrong data type of step")
while (True):
    try:
        n = int (input("Enter n="))
        if n < 1:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type of n(must be natural number)")

def prog(b, q, n, summ=0):
    if(n!=0):
        summ+=b*pow(q,n-1)
        return prog(b, q, n-1, summ)
    print("Summ={}".format(summ))

prog(b, q, n)