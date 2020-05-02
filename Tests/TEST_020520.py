import random
from random import randint

n = [random.randint(0, 100) for i in range(10)]
print (n)

def quicksort(n):
   if len(n) <= 1:
       return n
   else:
       q = random.choice(n)
       more = []
       less = []
       equal = []
       for n in n:
           if n < q:
               less.append(n)
           elif n > q:
               more.append(n)
           else:
               equal.append(n)
       return quicksort(less) + equal + quicksort(more)

print (quicksort(n))

def gnome(n):
    i = 1
    while i < len(n):
        if len(n) <= 1:
            return n
        elif (n[i - 1] <= n[i]):
            i += 1
        else:
            tmp = n[i]
            n[i] = n[i - 1]
            n[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return n

print (gnome(n))