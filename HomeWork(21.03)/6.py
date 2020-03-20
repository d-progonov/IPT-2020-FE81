N = input("Введите количество элементов: ")
k = input("Введите степень: ")
N = int(N)
k = int(k)
ans = 0
if N >= 1:
    for i in range(1,N+1):
        ans += i**k
    print(ans)    
else: print("error")    
