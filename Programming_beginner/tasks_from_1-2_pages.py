from collections import Counter
import math

# 1 - TASK

data = input("Input 5 digit num ")
for n in list(data):
    print(n)

# 2 - TASK

a = int(input("A = "))
b = int(input("B = "))
f = int(input("F = "))
print((a + b - (f / a)) + (f * a * a) - (a + b))

# 3 - TASK

print("+\n" + "+ +\n" + "+  +\n" + "+   +\n" + "+    +\n" + "+++++++")

# 4 - TASK

a = int(input("A = "))
b = int(input("B = "))
if a == b:
    print("equal")
else:
    if (a < b):
        print( "A < B")
    else:
        print( "B < A" )


# 5 - TASK

data = [int(input("first = ")), int(input("second = ")), int(input("third = "))]

def plus5(data):
    for n in data:
        for m in data:
            if n == m:
                data[0] += 5
                data[1] += 5
                data[2] += 5
                return data
    return data
print(plus5(data))


#6 - TASK

N = int(input("N = "))
k = int(input("k = "))
summ = 0

for i in range(1, N+1, 1):
     summ += pow(i, k)

print (summ)

# 7 - TASK

data = input("Num = ")
data_in_list = list(data)
int_data = [int(data_in_list[0]), int(data_in_list[1])]

print("max = " + str(max(int_data)))
print("min = " + str(min(int_data)))


# 8 - TASK

N = int(input("N = "))
k = int(input("k = "))
res = 1

for i in range(1, N+1, 1):
    res = res * k

print(res)


# 9 - TASK

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

print(math.sqrt((x)**2 + (y)**2 + (z)**2))


# 10 - TASK

x = int(input("x = "))
y = int(input("y = "))
print(pow(2, 3))
print(pow((1 - math.tan(x)), (math.cos(x)/math.sin(x)))+ math.cos(x-y))
