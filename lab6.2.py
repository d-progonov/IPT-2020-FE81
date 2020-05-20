import sys
import math
from lab62zad import file_data

sys.setrecursionlimit(20000)

def A(n,m):
    if n==0:
        return (m+1)
    elif n>0 and m==0:
        return A(n-1,1)
    elif n>0 and m>0:
        return A(n-1,A(n,m-1))

if __name__ =="__main__":
    res=file_data()
    if len(res)<2:
        print("Coeffs are not enough")
        exit()
    answ=A(res[0],res[1])
    f = open("output.txt", "a")
    f.write('{} '.format(str(answ)))