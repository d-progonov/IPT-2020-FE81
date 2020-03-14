import math
e = 10**(-4)
n = 1
res = 0
while (n**3)/(math.factorial(3*n-3)) > e:
    res += (n**3)/(math.factorial(3*n-3))
    n += 1
    print(round(res, 4))
print("Sum your series :", round(res, 4))

