from module1 import g, func

#A
s = float(input('s = '))
t = float(input('t = '))

print(g(1.2, t) + g(t,s) - g(2*s-1, s*t))

#B
n = int(input('n = '))
print (func (1, 2, n))
