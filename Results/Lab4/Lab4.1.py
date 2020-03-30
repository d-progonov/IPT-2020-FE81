n = input()
i = 1
t = 1
ans = []
def is_digit(temp):
    if temp.isdigit():
       return True
    else:        
        try:
            int(temp)
            return True
        except ValueError:
            print(temp,"not an intager")
            return False
if is_digit(n):
    n = int(n)    
    matr = []
    for j in range(n):
        matr.append([0] * n)
    
    for x in range(len(matr)):
        for y in range(len(matr[x])):            
            matr[x][y] = input("Enter value for matr[%s][%s]: "%(i,y+1))
        i += 1        
    for string in matr:
        for elem in string:
            print(elem,end="   ")
        print()
            
    for x in range(len(matr)):
        for y in range(t,len(matr[x])):
            if is_digit(matr[x][y]):
                matr[x][y] = int(matr[x][y])
                if matr[x][y] % 5 == 0:
                    ans.append("index: [%s][%s]"%(x+1,y+1))
        t += 1
    for i in range(len(ans)):
        print(ans[i])
else: print("Please use numbers")
        
