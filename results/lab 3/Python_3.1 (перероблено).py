N = input('N = ')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        N = input("Enter a number. N = ")

sum = 0
n = 1
#передумова
while n <= N:
    sum += (1/(2**n) + 1/(3**n))
    n += 1
 
print(round(sum, 4))

#постумова
sum = 0
n = 1
while True:
    sum += (1/(2**n) + 1/(3**n))
    n += 1
    if not n <= N:
        break

print(round(sum, 4))
