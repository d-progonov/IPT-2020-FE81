def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Ошибка, уведите целое или дробное число")
        check_help = False
    return check_help


def fraction(n):
    if n == 0:
        return 1
    else:
        ans = 1 + 1 / fraction(n - 1)
        return ans


while 1:
    n = input("Уведите количество знаменателей  ")
    if check(n) == False:
        continue
    if int(n) < 0:
        print("Число отрицательное")
        continue
    else:
        n = int(n)
        ans = fraction(n)
        print("Ответ ", ans)
        break