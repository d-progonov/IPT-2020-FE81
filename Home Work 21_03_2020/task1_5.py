def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Уведите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        num_1 = input("num_1 =  ")
        if check(num_1) == False:
            continue
        num_2 = input("num_2 =  ")
        if check(num_2) == False:
            continue
        num_3 = input("num_3 =  ")
        if check(num_3) == False:
            continue
        else:
            num_1 = float(num_1)
            num_2 = float(num_2)
            num_3 = float(num_3)
            if (num_1 == num_2) | (num_1 == num_3) | (num_2 == num_3):
                num_1 += 5
                num_2 += 5
                num_3 += 5
                print("num_1 = ", num_1, '\n' "num_2 = ", num_2, '\n' "num_3 = ", num_3, '\n')
        break


work()
