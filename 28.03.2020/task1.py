def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Ошибка, уведите целое или дробное число")
        check_help = False
    return check_help


def func(n):
    res = float((n - 1) / n)
    return res


def work():
    while 1:
        n = input("n =  ")
        if check(n) == False:
            continue
        if int(n) <= 0:
            print("Ошибка, невозможно такое количество чисел")
            continue
        else:
            sum = 0
            n = int(n)
            while n > 2:
                sum += func(n)
                n -= 1
                print("Поточне значення: " + str(sum))

        print("Остаточний результат: " + str(sum))
        break


if __name__ == "__main__":
    work()
