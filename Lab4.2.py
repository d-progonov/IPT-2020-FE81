import random
while(True):
    try:
        n = int(input("Enter size of array: "))
        if(n > 0):
            counter = 0
            array = []
            arrayTemp = []
            for i in range(n):
                array.append(random.randint(0,10))
            print(array)

            for i in range(n):
                arrayTemp.append(0)

            direction = int(input("Enter direction:\n1.Right\n2.Left\n"))
            start = int(input("Enter start point: \n"))
            b = start
            zeroPos = 0
            a = 0
            if(direction == 1 and start >= 0):
                while(True):

                    if(b < len(array)):
                        arrayTemp[a] = array[b]
                        b += 1
                        a += 1
                    elif(zeroPos < start):
                        arrayTemp[a] = array[zeroPos]
                        zeroPos +=1
                        a += 1
                    else:
                        break
                zeroPos = 0
                print(arrayTemp)
            elif(direction == 2 and start >= 0):
                zeroPos = len(array) - 1
                while(True):

                    if(b >= 0):
                        arrayTemp[a] = array[b]
                        b -= 1
                        a += 1
                    elif(zeroPos > start):
                        arrayTemp[a] = array[zeroPos]
                        zeroPos -= 1
                        a += 1
                    else:
                        break
                print(arrayTemp)
            else:
                print("Wrong direction")
        else:
            print("Wrong array size")
    except ValueError:
        print("Wrong data type")
