from random import randrange


def pair(num):
    return (num % 2) == 0


number = [randrange(start=0, stop=90, step=1) for i in range(10)]
print(number)
number.pop(0)
print(number)
i = 0
while i < len(number):
    if pair(number[i]):
        number.insert(i + 1, 0)
        i += 1
    i += 1
print(number)
