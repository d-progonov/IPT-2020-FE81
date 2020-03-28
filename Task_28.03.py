while(1):
    try:
        n = int (input("Enter n = "))
        1/(n+abs(n))
        break
    except Exception:
        print("Wrong data type for variable a (must be natural int).")
sum=0
while (True):
    if (n<1):
        break
    sum+=(n-1)/n
    n -= 1

print("S = {:0.4f}".format(sum))
input("Any key to exit...")