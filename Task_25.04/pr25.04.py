a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
 
for x in range(1,d//a):
    for y in range(1,d//b):
        for z in range(1,d//c):
            if x*a + y*b + z*c == d:
                print("%d*%d + %d*%d + %d*%d = %d" % (a,x,b,y,c,z,d))
