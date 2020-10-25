res_nums = list()

for i in range(200, 301):
    sum_a = 0
    sum_b = 0

    if i in res_nums:
        continue

    for n in range(1,i):
        if i % n == 0:
            sum_a += n
    
    if sum_a <= 300 and sum_a >= 200:
        for k in range(1, sum_a):
            if sum_a % k == 0:
                sum_b += k
    else:
        continue
    
    if sum_b <= 300 and sum_b >= 200:
        if i == sum_b:
            print("Needed numbers are:", i, "and", sum_a)
            res_nums.append(sum_a)
            res_nums.append(i)

