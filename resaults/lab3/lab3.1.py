import math

N = input('N = ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        N = input("Enter a number. N = ")

def a(n):
    return pow(-1, n - 1)/pow(n, n)

S = 0
n = 1

while n <= N:
    S += a(n)
    n += 1

print (round(S, 4))
