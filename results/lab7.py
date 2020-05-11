n = input("Enter n:")
m = input("Enter m:")
a=[]
try:
    n = int(n)
    m = int(m)
    for i in range(n):
        temp = False

        while(temp==False):
            x=input("Enter your string with "+ str(m) +" symbols:")
            if(len(x)==m):
                temp=True
                a.append(x)
            else:
                print("I said "+str(m)+" symbols")

    print(a)
    for row in a:
        print(' '.join([str(ord(str(elem))) for elem in row]))

except ValueError:
    print("Введите другое значаение для n!!!")

