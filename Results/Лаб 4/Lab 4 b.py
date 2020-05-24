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

                n = int(input("Введите размерность масива:"))

                if n < 1:

                    print("количество элементов не может быть меньше 1")

                else:

                    break

        except ValueError:

            print("Неверное значение")

        else:

            break



    for i in range(n):

        L.append(random.randint(1, 100))



    print(L)



    swap(L)



    print(L)

    print("Средний элемент =", sum(L)/len(L))



    for j in range(n):

        if L[j]-1.1*sum(L)/len(L) > 0:

            IndexMas.append(j)



    

    for i in range(len(IndexMas)):

        L.pop(IndexMas[i]-i)



    print(L)

