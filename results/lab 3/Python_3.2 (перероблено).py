import math
def primnum(N):
  num = set(range(1, N))
  for i in range(2, int(math.sqrt(N))):
    if i in num:
      num -= set(range(2*i, N, i))
  return num

n = int(input('n = '))

List = list(primnum(n))
for k in List:
    print (2**k -1)
