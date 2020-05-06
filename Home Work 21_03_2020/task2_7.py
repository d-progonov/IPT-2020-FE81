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
        n = input("Уведите размер последовательности:  ")
        if check(n) == False:
            continue
        k = input("Иднекс искаемого елемента =  ")
        if check(k) == False:
            continue
        if k > n:
            print("Ошибка, индекс попал за границу масива!")
            continue
        else:
            n = int(n)
        arr = []
        while n > 0:
            num = input("Уведите число: ")
            if check(num) == False:
                continue
            else:
                num = int(num)
                arr.append(num)
                print(arr)
                n -= 1
        k = int(k)
        print("Искаемое число: ", arr[k-1])

        break


if __name__ == "__main__":
    work()
