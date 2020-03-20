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
        print("Уведите числа в порядке: 1 - а, 2 - b, 3 - f")
        a = input("a =  ")
        if check(a) == False:
            continue
        if int(a) == 0:
            print("на 0 делить нельзя")
            continue
        b = input("b =  ")
        f = input("f =  ")
        if check(b) == False:
            continue
        if check(f) == False:
            continue
        else:
            a = float(a)
            b = float(b)
            f = float(f)
            ans = ((a + b - f) / a) + f * a ** 2 - (a + b)
            print(ans)
        break


work()
