x = input("Введіть число: ")
x = float(x)
k = input("Введіть степінь: ")
k = int(k)
ans = x
if k >= 1:
    for i in range(1,k):
        ans *= x
    print(ans)
else: print("Error")
