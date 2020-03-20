from copy import copy
while (True):
    try:
        m=float(input("Enter m ="))
        break
    except ValueError:
        print("Wrong data type of m")
while (True):
    try:
        n=int(input("Enter n ="))
        if n<1:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type of n(must be natural number)")
a=copy(m)
for i in range(1,n):
    m*=a
print("Result = {}".format(m))