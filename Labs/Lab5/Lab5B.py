n = abs(int(input("Введите натуральное число n: ")))
m = abs(int(input("Введите натуральное число m: ")))

def ncd(n, m):
    if m == 0: 
        return n
    else: 
        return ncd(m, n % m)  
print(ncd(n,m))



