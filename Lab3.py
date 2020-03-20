import math 
def func():
    try:
        N = int(input("Количество єлементвов: "))
        sum = 0
        n = 0
        while n < N:
            curr = math.log(math.factorial(n))*(math.exp((-n)*math.sqrt(n)))
            sum = sum + curr
            n = n + 1
        print("%.4f" % sum)  # e = 10^(-4)
    except ValueError:
        print("Неправильные данные")
func()
