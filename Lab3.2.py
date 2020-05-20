import random
while(True):
    try:
        n = int (input("Enter n = "))
        if(n > 0):
            i = 0
            array = list()
            count = 0
            a = 0
            for a in range(n):
                array.append(random.randint(0,10))
            print(array)
            for i in range(n):
                if(array[i] % 2 != 0 and i % 2 == 0):
                    count += 1
                    print("Value:",array[i], " Index: ", i)
            print("Amount of right numbers",count)
        else:
            print("Wrong array size, enter number > 0")
    except ValueError:
        print("Wrong data type")
