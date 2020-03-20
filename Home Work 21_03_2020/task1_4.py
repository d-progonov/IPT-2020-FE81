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
        num_1 = input("num1 =  ")
        if check(num_1) == False:
            continue
        num_2 = input("num2 =  ")
        if check(num_2) == False:
            continue
        else:
            num_1 = float(num_1)
            num_2 = float(num_2)
            if num_1 > num_2:
                print("Больше")
            if num_1 < num_2:
                print("Меньше")
            if num_1 == num_2:
                print("Эти числа равны")
        break


work()
