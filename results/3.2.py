n = 100
out = []
i = 1

def isPrime(n):
    if n <= 1: return False
    for i in range(2, n): return (n % i) != 0


while True:
    num  = 2**i-1
    if isPrime(num):
        if num>n:
            break
        out.append(num)
    i+= 1
print(out)
