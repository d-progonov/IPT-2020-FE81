'''
Найти алгебраическую сумму для выражения: 
1^k + 2^k + 3^k + ... + N^k. 
N и степень k вводит
пользователь.
'''

N  = int(input("Input number of elem: ")) 
k  = int(input("Input power of elem: "))

sum = 0
for i in range(N+1):
    elem = pow(i, k)
    sum = sum + elem

print(sum)
