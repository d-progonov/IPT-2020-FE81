import numpy as np


def work():
    while 1:
        bool = False
        if bool == False:
            s = str(input("Уведите сроковую константу: "))
            arr = list(s.split())
            print(arr)
            bool = True
            k = np.size(arr)
            for i in range(0, k, 1):
                if len(arr[i]) <= 1:
                    bool = False
                    print("Длина " + str(i + 1) + " слова равна 1 символу.")
                    break
                else:
                    bool = True
            if bool == True:
                k = np.size(arr)
                z = []
                for i in range(0, k, 1):
                    if arr[i][1] == 'a':
                        z.append(arr[i])
                current = 0
                k = np.size(z)
                for i in range(0,k,1):
                    if len(z[current]) <= len(z[i]):
                        current = i
                        print(z[current])
                print("Cамое длинное слово: " + str(z[current]))
                break


work()
