import random

arrr = [random.randint(0, 100) for i in range(10)]
print(arrr)

i = 0

while i < 20:

    if arrr [i] % 2 == 0:
        arrr.insert(i+1, arrr[i-1]+2)
        i += 1
    i += 1
    if  len(arrr) == i:
        break
  
print (arrr)

i = 0

while i < 10:

    if arrr [i] == 0:
        arrr.pop(i)
        print (arrr)
        break

    i += 1


else:
    print ('There is no element that is equal to zero')
