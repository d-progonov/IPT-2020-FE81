from math import sqrt 

N = input('N = ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        N = input("Enter a number . N = ")

S = 0
factorial = 1

for i in range(1, N+1):
    factorial *= i
    S += factorial/pow(i,sqrt(i))

print (S)

