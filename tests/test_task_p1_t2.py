print("Please input the numbers in the next order: 1. a, 2. b, 3.f.\n1. a:")
a = float(input())
print("2. b:")
b = float(input())
print("3. f:")
f = float(input())

k = (a + b - f / a) + f * a * a - (a + b)

print(str(k))