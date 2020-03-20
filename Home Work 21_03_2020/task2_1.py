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
        n = input("n =  ")
        if check(n) == False:
            continue
        k = input("k =  ")
        if check(k) == False:
            continue
        else:
            n = int(n)
            k = int(k)
            i = 0
            sum = 0
            while i <= n:
                sum += i ** k
                i += 1
                print("Сума = {}".format(sum))
            print("Остаточный результат = {}".format(sum))
        break


work()
