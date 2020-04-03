import func


def work():
    while 1:
        try:
            file = open('text.txt', 'r')
        except Exception:
            print("Невозможно найти путь к файлу")
            continue

        m = int(file.readline())
        print(m)
        a = int(file.readline())
        print(a)
        c = int(file.readline())
        print(c)
        file.close()

        res = 0
        res = func.f(m, a, c)
        print("Остаточный результат:  " + str(res))
        ans = open('ans.txt', 'w')
        ans.write("Остаточный ответ:  " + str(res))
        ans.close()
        break


if __name__ == "__main__":
    work()
