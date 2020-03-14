def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Error.a, уведите целое или дробное число")
        check_help = False


def work():
    while 1:
        num = input("num = ")
        if check(num) == False:
            continue
        else:
            num = float(num)
            if num >= 0:
                num *= 3
                print(num)
            if num < 0:
                num = num ** 2
                print(num)
            break
work()
