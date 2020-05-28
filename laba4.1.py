import random
import math

def task():
    while 1:
        try:
            N=int(input('Enter a size of matrix: '))
        except ValueError:
            print("Error; enter an integer number.")
            continue
        if N <= 0:
            print("Error; Number must be positive")
            continue
        if math.isinf(N):
            print("Error; number can not be an infinite")
            continue
        if math.isnan(N):
            print("Error; number must an integer")
            continue
        else:
            break
    array=[random.randint(1,100) for _ in range(N)]
    for i in range(len(array)):
        print(array[i], end=' ')
    while 1:
        try:
            remove = int(input('\nEnter a number to remove: '))
        except ValueError:
            print("Error; enter an integer number.")
            continue
        if remove<=0:
            print("Number must be positive")
            continue
        if math.isinf(N):
            print("number can not be an infinite")
            continue
        if math.isnan(N):
            print("number must an integer")
            continue
        else:
            break
    if(remove>N) or (remove<0):
        print("Error; this number is out of range")
    array.pop(remove-1)
    for i in range(len(array)):
        print(array[i], end=' ')
    for i in range(len(array)):
        if array[i]%2==0:
            index=i
            break
    new_element=array[index-1]+2
    array.insert(index+1,new_element)
    print("\nNow, matrix is:   \n")
    for i in range(len(array)):
        print(array[i], end=' ')

if __name__=="__main__":
    task()