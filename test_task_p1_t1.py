print("Please, print the number")

a = int(input())
i = 1

for i in range (0, 5):
    print(str(int(a%10)))
    a /= 10