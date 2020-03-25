import math

e = 10**(-4)

n = 1
res = 0
while ((2**n)*math.factorial(n))/(n**n) > e:
    res += ((2**n)*math.factorial(n))/(n**n)
    n += 1
    print(round(res, 4))
print("Sum your series :", round(res, 4))
