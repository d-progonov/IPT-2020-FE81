import random
import math

def posledov():
    while 1:
        try:
            N=int(input('Enter a size of sequence: '))
        except ValueError:
            print("Enter an integer number")
            continue
        if N <= 0:
            print("Number must be posotive")
            continue
        if math.isinf(N):
            print("Number can not be an integer")
            continue
        if math.isnan(N):
            print("Number must be integer")
            continue
        else:
            break
    array=[random.randint(1,100) for _ in range(N)]
    return array

def maxim_change(array):
    for i in range(len(array)):
        array1[i]=array[i]
    max_i=max(array1)
    for i in range(len(array1)):
        if max_i==array1[i]:
            index=i
    for i in range(index+1,len(array1)):
        array1[i]=0.5
    for i in range(len(array1)):
        print(array1[i], end=' ')
    print()

if __name__=="__main__":
    array1=posledov()
    array2=posledov()
    for i in range(len(array1)):
        print(array1[i], end=' ')
    print()
    for i in range(len(array2)):
        print(array2[i], end=' ')
    print()
    maxim_change(array1)
    maxim_change(array2)
