class NaturalError(Exception):
    pass
while (True):
    try:
        n=int(input("Enter N ="))
        if n<1:
            raise NaturalError
        break
    except ValueError:
        print("Wrong data type of N")
    except NaturalError:
        print("N must be natural")

while (True):
    try:
        k=float(input("Enter k ="))
        break
    except ValueError:
        print("Wrong data type of k")
a=0
for i in range(1,n+1):
    a+=pow(i,k)
print("Result = {}".format(a))
