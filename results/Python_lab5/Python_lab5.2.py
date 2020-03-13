while(1):
    try:
        n = int (input("Enter n = "))
        1/(n+abs(n))
        break
    except Exception:
        print("Wrong data type for variable n (must be natural int).")
while(1):
    try:
        m = int (input("Enter m = "))
        1/(m+abs(m))
        break
    except Exception:
        print("Wrong data type for variable m (must be natural int).")

def Euclidean(a,b):
    if (a%b)==0:
        return b
    else:
        return Euclidean(b,(a%b))

print("Greatest common divisor of {} and {} is".format(n,m), Euclidean(n,m))
input("Any key to exit...")