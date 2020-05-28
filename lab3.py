import math

''' Lab3'''

def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
def An(x):#Fuction to calc the sequence element
    return fact(x)/fact(2*x)
    
def circle1(exp): #setting up a precondition
    x=0 #Initialization of sequnce
    res=An(x)
    x=x+1
    res1=0
    while math.fabs(res-res1)>=exp:
        res+=An(x)#Calc An with result
        res1+=An(x-1)
        print("Now result is {} x is {}".format(res,x))
        x+=1 #Then increase x
    print("The answer is: {}".format(res))

def circle2(exp):
    x=0 
    res=An(x)
    x=x+1
    res1=0
    while 1:
        if math.fabs(res-res1) >= exp:
            res+=An(x)
            res1+=An(x-1)
            print("Now result is {} x is {}".format(res,x))
            x += 1  
        else:
            break
    print("The answer is: {}".format(res))

def for3():

    for x in range(1,101):
        x=str(x)
        if x==x[::-1]:
            print("{} is a palyndrom".format(x))

def Accuracy():
    while 1:
        try:
            exp=float(input("Enter an accuracy rate: "))
        except ValueError:
            print("Enter a number.")
            continue
        if math.isnan(exp) or exp<0 or exp==0 or math.isinf(exp):
            print("Error, try again.")
            continue
        return exp
if __name__ == "__main__":
    exp=Accuracy()
    circle1(exp)
    circle2(exp)
    for3()
        
   
    
