def func(u,v,w):
    return ((2*u)+(((3*u)*w)/((2+w)-u))-(7*v))

def fonc(n,x):
    if n==0:
        return 1
    elif n < 0:
        return (x ** n) + fonc(n+1,x)
    else:
        return (x ** n) + fonc(n-1,x)
    print (fonc(n,x))
