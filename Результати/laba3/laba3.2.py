x = 18 % 21

print("Task number:", x)

solution = []

while True:
    try:
        N = input("n = ")
        n = int(N)
        if n == 0:
            print("Your arg is '0' pick another one, please")
            continue
        if n < 0:
            print("Error! Natural numbers only! Input another one, please:")
            continue
        if n % 1 == 0:
            for q in range(1, n + 1):
                if n % q ** 2 == 0 and not n % q ** 3 == 0:
                    solution.append(q)
                else:
                    continue
        break
    except ValueError:
        print("Invalid value entered!")

if len(solution) == 0:
    print("There are no such 'q' for your value")
else:
    print("Such 'q' suit for your value:", solution)
