while(1):
    try:
        N = int (input("Enter N = "))
        if N<1:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable N (must be natural int).")
while(1):
    try:
        k = float (input("Enter k = "))
        break
    except ValueError:
        print("Wrong data type for variable k (must be float).")

s = 0;
for i in range(1,N+1):
    s += pow(i,k)
print("S =", s)
input("Any key to exit...")