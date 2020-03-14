import math

excelent = 10 ** (-4)
sum = 0.0
n = 1


def func(n):
    res = float(math.factorial(n - 1))
    res = float(res * 10 ** (-n))
    return res


while abs(func(n)) > excelent:
    sum += func(n)
    n += 1
    print("Поточне значення: " + str(sum))

print("Остаточний результат: " + str(sum))
