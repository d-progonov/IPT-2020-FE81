def func (a, d, n):
    if n == 1:
        return a
    else:
        return a + (n-1) * d + func (a, d, n-1)
 
n = int(input('n = '))
print (func (1, 2, n))