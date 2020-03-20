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
        num = input("num = ")
        if check(num) == False:
            continue
        if abs(int(num)) == False:
            continue
        if abs(int(num)) < 10000:
            print("Уведите число с заданого промежутка")
            continue
        if abs(int(num)) > 99999:
            print("Уведите число с заданого промежутка")
            continue
        else:
            num = abs(float(num))
            i = 10000
            while (i >= 1):
                print(int(((num - (num % i)) / i) % 10))
                i /= 10
        break


work()
