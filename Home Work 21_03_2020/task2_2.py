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
        print("Уведите двухзначное число")
        num = input("num =  ")
        if check(num) == False:
            continue
        if (float(num) > 99) or (float(num) < 10):
            print("Даное число не есть двухзначным")
        else:
            num = int(num)
            a = int(num / 10)
            b = int(num % 10)
            min_value = min(a, b)
            max_value = max(a, b)
            print("Минимальное значение = ", min_value, '\n' "Максимальное значение = ", max_value, '\n')
            break


work()
