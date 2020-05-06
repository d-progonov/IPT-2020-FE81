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
        n = input("n = ")
        if check(n) == False:
            continue
        else:
            n = math.radians(int(n))
            while n < 0:
                n = 2 * (math.pi)
            while n >= 2 * (math.pi):
                n -= 2 * (math.pi)

            sum = 0
            for i in range(1, n + 1):
                curr = 0
                for j in range(1, i + 1):
                    curr += 1 / math.sin(j)
                sum += curr
            print(sum)
        break


if __name__ == '__main__':
    work()
