input_str = []
temp = {}

for i in range(int(input("Введите количество строк: "))):
    input_str.append(input("Введите строку: "))

input_str.sort()

for i in input_str:
    if len(i) in temp.keys():
        temp[len(i)] = temp[len(i)] + f", {i}"
    else:
        temp[len(i)] = i

keys = list(temp.keys())
keys.sort()

for i in range(len(keys)):
    for j in temp[keys[i]].split(", "):
        print(j)

