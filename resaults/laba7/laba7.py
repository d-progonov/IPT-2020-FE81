import numpy as np 

def printX(mat):
    for i in range(len(mat)):
        print(mat[i])


c_str=input('Ведите строку: ')
mat=[]
l = len(c_str)

for i in range(l):
    mat.append([0 for i in range(l)])

for i in range(l-1):
    for j in range(l-1):
        if i == j:
            mat[i+1][j]=c_str[i]
            mat[i][j]=c_str[i]
            mat[i][j+1]=c_str[i]

    mat[l-1][l-1]=c_str[-1]     

printX(mat)   
mat = np.transpose(mat)
printX(mat)    
s1=""
s2=""

for i in range(l-1):
    for j in range(l-1):
        if i == j:
            s1+=mat[i+1][j]
            s2+=mat[i][j+1]

print(s1+s2)
