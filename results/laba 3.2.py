import math

n=input("Enter n:")
a=0
Prime=[]

try:
    n=int(n)
    if(n>0):
        j=2
        for i in range(1,n):
            if(n%i==0):
                #print(i)
                if i==1 or i==2:
                    Prime.append(i)
                else:

                    for j in range(2,i):
                        if(i%j==0):
                            #print(i,"is not a prime")
                            j+=1
                            break
                        else:
                            Prime.append(i)
                            j+=1
                            break

                # if(i==1 or i==2):
                #     Prime.append(i)
                # else:
                # for j in range(2,i):
                #         if(i%j==0):
                #             a+=1
                #             break
                #         else:
                #             Prime.append(i)
    print(Prime)

except ValueError:print("Введите другое значаение для n!!!")