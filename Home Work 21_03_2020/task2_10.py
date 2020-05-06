import math


def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Ошибка, уведите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        a = input("a = ")
        if check(a) == False:
            continue
        b = input("b = ")
        if check(b) == False:
            continue
        c = input("c = ")
        if check(c) == False:
            continue
        d = input("d = ")
        if check(d) == False:
            continue
        k = input("k = ")
        if check(k) == False:
            continue
        else:
            a = float(a)
            b = float(b)
            c = float(c)
            d = float(d)
            k = float(k)

            discrim = (b - d) ** 2 - 4 * a * (c - k)
            if discrim < 0:
                print("Ошибка, зашли в комплексную область")
            elif discrim == 0:
                x0 = (d - b) / (2 * a)
                print("1) ({}, {})".format(x0, d * x0 + k))
            else:
                x1 = ((d - b) + math.sqrt(discrim)) / (2 * a)
                x2 = ((d - b) - math.sqrt(discrim)) / (2 * a)
                print("1) {}, {}".format(x1, d * x1 + k))
                print("2) {}, {}".format(x2, d * x2 + k))
            break


if __name__ == "__main__":
    work()
