def check(NUM):
    check_help = True
    try:
        num_1 = int(NUM)
    except ValueError:
        print("Error, уведите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        n = input("n = ")
        if check(n) == False:
            continue
        else:
            n = int(n)
            for i in range(0, n, 1):
                if ((i % 7 == 1) | (i % 7 == 2) | (i % 7 == 5)):
                    print(i)
            break


work()
