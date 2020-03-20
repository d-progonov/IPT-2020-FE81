def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Error, уведите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        print("Уведите числа n - число, k - его степень")
        n = input("n =  ")
        if check(n) == False:
            continue
        k = input("k =  ")
        if check(k) == False:
            continue
        else:
            n = float(n)
            k = int(k)
            mult = 1
            for i in range(1, k + 1, 1):
                mult *= n
                print("Поточное значение", mult)
            print("Остаточное значение ", mult)
        break


work()
