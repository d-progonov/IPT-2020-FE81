import math
n = int(input("Кількість елементів = : "))
sum = 0
i = 1
while i <= n:
    a = (10**i)/(math.factorial(i))
    print(i,"- element is: ", a)
    sum = sum + a
    i = i + 1
print(float("{0:.4f}".format(sum)))

