from math import factorial
i=0
a=0
k=1
while(abs(k)>=0.0001):
    k=pow(3,i)*factorial(i)/factorial(3*i)
    print("A({0})={1}".format(i,k))
    a+=k
    i+=1
print("Summ={:0.4f}".format(a-k))