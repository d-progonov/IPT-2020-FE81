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
        num = input("num = ")
        if check(num) == False:
            continue
        k = input("k = ")
        if check(k) == False:
            continue
        else:
            if len(num) < int(k):
                k = len(num)
            else:
                k = int(k)
            num_l = list(num)
            print(num_l)
            ans = []
            i = 0
            while i < k:
                ans.append(num_l[i])
                i += 1
            print(ans)
            number = ''.join(ans)
            print(number)
            break


if __name__ == "__main__":
    work()
