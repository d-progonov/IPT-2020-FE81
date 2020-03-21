def g(a, b):
    return (a**2 + b**2)/(a**2 + 2*a*b + 3*(b**2) + 4)

def func (a, d, n):
    if n == 1:
        return a
    else:
        return a + (n-1) * d + func (a, d, n-1)
