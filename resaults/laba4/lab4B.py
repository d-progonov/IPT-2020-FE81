import random
M = []
IM = []

def swap(m):
    imin = m.index(min(m))
    imax = m.index(max(m))
    m[imax], M[imin] = m[imin], m[imax]

if __name__ == '__main__':

    while True:
        try:
            while True:
                n = int(input("Введите количество элементов:"))
                if n < 1:
                    print("Номер элемента не может быть 1")
                else:
                    break
        except ValueError:
            print("Неверный ввод")
        else:
            break

    for i in range(n):
        M.append(random.randint(1, 100))

    print(M)

    swap(M)

    print(M)
    print("Среднее значение =", sum(M)/len(M))

    for j in range(n):
        if M[j]-1.1*sum(M)/len(M) > 0:
            IM.append(j)

    for i in range(len(IM)):
        M.pop(IM[i]-i)

    print(M)

