def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Ошибка, уведите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        n = input("n = ")
        if check(n) == False:
            continue
        else:
            n = int(n)
            sum = 0
            i = 0
            while i <= n:
                if i % 5 == 0:
                    sum += i
                i += 1
            print("Сумма всех чисел", sum)
            break


if __name__ == "__main__":
    work()
