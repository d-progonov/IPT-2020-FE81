import math

a = 18%25

while True:
     try:
         X=input("Input your value: x=")
         if X=="inf":
             x=float('inf')
         elif X=="nan":
             print("Not a number! Input a value,please:")
             continue
           x=float(X)
           break
       except ValueError:
           print("Invalid value entered!")

while True:
     try:
         Z=input("Input your value:z=")
         if Z=="inf":
             z=float('inf')
         elif Z=="nan":
            print("Not a number! Input a value,please:")
            continue
          z=float(Z)
          break
      except ValueError:
          print("Invalid value entered!")

if __name__=='__main__':
    print("Task number:",a)
    if x==z==float('inf'):
        print("Impossible to get an answer with 2 infinities!")
        exit(0)
    elif z or x==float('inf'):
        print("The answer is: Infinity")
        exit(0)
        
    if not (x < -3 or x >3):
        print ("Error!")
    else:
        y = abs(x ** 3 - z ** 3) / math.sqrt(x ** 2 - 9)
        print(y)
        
