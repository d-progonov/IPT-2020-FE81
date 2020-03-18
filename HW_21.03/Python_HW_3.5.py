class Error(Exception):
    pass

def firstKofN(k, n):
    try:
        k = int(k)
        n = int(n)
        n = str(abs(n))
        if k<=0:
            raise Error
        if k>len(n):
            raise Error
    except ValueError:
        print("Arguments must be integers.")
        return
    except Error:
        print("Unable to get {} first numbers of {}.".format(k, n))
        return
    ans = 0;
    i = 1
    while(k!=0):
        ans+=int(n[k-1])*i
        i*=10
        k-=1
    return(ans)

print(firstKofN(2,"jhg"))
print(firstKofN(-5,0))
print(firstKofN(0,123))
print(firstKofN(3,15645))
print(firstKofN(4,21))
print(firstKofN(4,-21123))
print(firstKofN(5,21021))

input("Any key to exit...")

