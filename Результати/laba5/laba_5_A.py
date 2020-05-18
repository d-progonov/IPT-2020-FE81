while True:
    try:
        n = int(input("Input any natural number for checking:"))
        if n <= 0:
            print("Natural numbers only excepted! input another value, please")
            continue
        break
    except ValueError:
        print("Invalid value entered!")


def task(taken):
    result = []
    for i in range(len(taken) - 1):
        if taken[i] == taken[i + 1] - 2:
            result.append((taken[i], taken[i + 1]))
    return result

def prime_check(n):
    print("Number for checking is:", n, '\n')
    numbers = list(range(2, 2 * n + 1))
    for i in numbers:
        if i != 0:
            for k in range(2 * i, 2 * n + 1, i):
                numbers[k - 2] = 0

    primes = [x for x in numbers if x != 0]
    print("Prime numbers list:", primes, '\n')
    result = task(primes)
    if len(result) == 0:
        print("There are no twin numbers!")
    print(result)

if __name__ == '__main__':
    prime_check(n)
