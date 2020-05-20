import sys
import math

sys.setrecursionlimit(20000)

def coef():
    while 1:
        try:
            n=int(input("Enter a positive number: "))
        except ValueError:
            print("Error,number must be an integer. ")
        if n<0:
            print("Error,number must be a positive.")
            continue
        if math.isnan(n):
            print("Error, number muxt be an integer")
            continue
        if math.isinf(n):
            print("Number can not be an infinite")
            continue
        else:
            break
    return n

def A(n,m):
    if n==0:
        return (m+1)
    elif n>0 and m==0:
        return A(n-1,1)
    elif n>0 and m>0:
        return A(n-1,A(n,m-1))

if __name__ =="__main__":
    n=coef()
    m=coef()
    print(A(n,m))