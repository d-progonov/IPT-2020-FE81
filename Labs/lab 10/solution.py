import math

n = math.fabs(int(input("Enter N: ")))

def euler_function(n):
    ret = 1
    for i in range(2, math.floor(n**0.5)):
        p = 1
        while not n % i:
            p *= i
            n /= i
        p /= i
        if p >= 1:
            ret = ret * p * (i - 1)
    n -= 1
    return n * ret if n else ret

print(euler_function(n))
