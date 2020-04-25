input_values = [2, 3, 4, 5]


class Ref:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)



nums = [el ** i for i in range(1, len(input_values) + 1) for el in input_values]
size = len(input_values)

matrix = [[Ref(0) for j in range(size)] for i in range(size)]

zigzagged = [[] for i in range(size * 2 - 1)]

for i in range(size):
    for j in range(size):
        sum = i + j
        if sum % 2 == 0:
            zigzagged[sum].insert(0, matrix[i][j])
        else:
            zigzagged[sum].append(matrix[i][j])

zigzagged = [e for r in zigzagged for e in r]

for i in range(len(nums)):
    zigzagged[i].value = nums[i]
print("Input: " + str(input_values))
print("Computed to fill matrix: "+str(nums))
print("Zig-zag matrix: ")
for r in matrix:
    print(r)
