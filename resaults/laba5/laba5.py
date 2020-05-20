# A
def p(x, Ar):
    sum1 = 0
    for i in range(0, 7):
        elem = (Ar[i])*x**i
        sum1 += elem
    return sum1

def polinome(A):
    pol1= p(2, A) - p(1, A) 
    print("Результат полинома при х=1:", pol1)
    pol3 = p(4, A) - p(3, A) 
    print("Результат полиному при х=3:", pol3)
    pol4 = p(5, A) - p(4, A) 
    print("Результат полинома при х=4:", pol4)

try:
    print("Ведите элементы a0 до a6: ")
    A1 = [float(input("Элемент сейчас: ")) for i in range(0, 7)]

    polinome(A1)
    
except ValueError:
    print("Ошибка, введите число.")

# B
def sum(N, b, q):
    return (b*(1-pow(q,N)))/(1-q)

try:
    n = abs(int(input("Количество элементов в прогрессии: ")))
    if n != 0:
        b = float(input("Первый элемент прогрессии: "))
        if n == 1:
            print("В прогрессии всего 1 элемент, сумма -", b)
        else:
           q = float(input("Знаменатель прогрессии (НЕ равен 1): "))
           print("Сумма",n, "членов геометрической прогрессии -", round(sum(n, b, q),3))
    else:
        print("В данной прогрессии 0 элементов, сумма - 0")

except ValueError:
    print("Ошибка! Введите натуральное число!")
