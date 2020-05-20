# A
def p(x, Ar):
    sum1 = 0
    for i in range(0, 7):
        elem = (Ar[i])*x**i
        sum1 += elem
    return sum1

def polinome(A):
    pol1 = p(2, A) - p(1, A) 
    print("Результат полинома при х=1:", pol1)
    pol3 = p(4, A) - p(3, A) 
    print("Результат полиному при х=3:", pol3)
    pol4 = p(5, A) - p(4, A) 
    print("Результат полинома при х=4:", pol4)

# B
def sum(N, b, q):
    return (b*(1-pow(q,N)))/(1-q)
