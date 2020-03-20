import math


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
        x = input("X (у градусах) =  ")
        if check(x) == False:
            continue
        y = input("Y (у градусах) =  ")
        if check(y) == False:
            continue
        x = float(x)
        y = float(y)
        x = math.radians(x)
        y = math.radians(y)
        # Переводим у промежуток переменные [0; 2*pi]

        while x < 0:
            x = 2 * (math.pi)
        while x > 2 * (math.pi):
            x -= 2 * (math.pi)
        print(x)

        while y < 0:
            y = 2 * (math.pi)
        while y >= 2 * (math.pi):
            y -= 2 * (math.pi)
        print(y)
        if y == 0 or y == math.pi or x == 0 or x == math.pi:
            print("На ноль делить нельзя")
            continue
        else:
            ctg = math.cos(y) / math.sin(y)
            ans = pow(1 - math.tan(x), ctg) + math.cos(x - y)
            print(ans)
        break


work()
