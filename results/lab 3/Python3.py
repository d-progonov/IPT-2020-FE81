N = input('N = ')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        N = input("Enter a number. N = ")

sum = 0

for n in range(1, N+1):
    sum += (1/(2**n) + 1/(3**n))
 
print(round(sum, 4))
