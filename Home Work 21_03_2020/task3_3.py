import random


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
        n = input("n = ")
        if check(n) == False:
            continue
        else:
            n = int(n)
            list = [random.randint(-100, 100) for i in range(n)]
            print("Входной масив: ", list)
            odd_num = []
            for elem in list:
                if elem % 2 != 0:
                    odd_num.append(elem)
                elem += 1
            print("Масив с непарных чисел: ", odd_num)
            break

if __name__ == "__main__":
    work()
