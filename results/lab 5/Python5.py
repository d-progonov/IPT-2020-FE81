def g(a, b):
    return (a**2 + b**2)/(a**2 + 2*a*b + 3*(b**2) + 4)

s = float(input('s = '))
t = float(input('t = '))

print(g(1.2, t) + g(t,s) - g(2*s-1, s*t))