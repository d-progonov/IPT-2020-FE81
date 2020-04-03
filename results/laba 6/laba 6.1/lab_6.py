from func import check, square
import numpy as np


def work():
    while 1:
        try:
            file = open('text.txt', 'r')
        except Exception:
            print("Невозможно найти путь к файлу")
            continue

        n = int(file.readline())
        print(n)
        x = []
        y = []
        z = []
        while n > 0:
            x.append(float(file.readline()))
            y.append(float(file.readline()))
            print(x, y, sep='\n')
            n -= 1
        file.close()
        res = 0
        k = np.size(x)
        for i in range(0, k, 1):
            if i == (k - 1):
                z.append(square(x[0], x[k - 1], y[1], y[k - 1]))
            else:
                z.append(square(x[i], x[i + 1], y[i], y[i + 1]))
            res += z[i]
        print("Площадь н-угольника ровняется: " + str(res))
        f = open('ans.txt', 'w')
        f.write("Остаточный ответ:  " + str(res))
        f.close()

        break


if __name__ == "__main__":
    work()
