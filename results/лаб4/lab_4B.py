import random
L = []
IndexMas = []


def swap(l):
    imn = l.index(min(l))
    imx = l.index(max(l))
    l[imx], L[imn] = l[imn], l[imx]


if __name__ == '__main__':

    while True:
        try:
            while True:
                n = int(input("Enter number of elements:"))
                if n < 1:
                    print("number of elements can not be less than 1")
                else:
                    break
        except ValueError:
            print("Invalid value")
        else:
            break

    for i in range(n):
        L.append(random.randint(1, 100))

    print(L)

    swap(L)

    print(L)
    print("average =", sum(L)/len(L))

    for j in range(n):
        if L[j]-1.1*sum(L)/len(L) > 0:
            IndexMas.append(j)

    # print(IndexMas)
    for i in range(len(IndexMas)):
        L.pop(IndexMas[i]-i)

    print(L)



