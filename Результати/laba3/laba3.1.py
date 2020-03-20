
import math

n = 2

while n <= 15:
    a = n ** math.log(n) / math.log(n) ** n
    a += a
    n += 1
print(a)


import math

n = 2

while True:
    a = n ** math.log(n) / math.log(n) ** n
    a += a
    n += 1
    if n > 15:
        break
print(a)
