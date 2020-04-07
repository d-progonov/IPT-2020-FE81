while True:
    try:
        N = float(input("Input boundary even value not including '2':"))
        if N == "nan":
            print("Can‘t be Not a Number")
            continue
        elif N == float('inf'):
            print("Infinity not excepted!")
            continue

        n = float(N)
        if n - int(n) == 0:
            n = int(n)
            if n % 2 != 0:
                print("Please, input even number")
                continue
            elif n < 0:
                print("Positive even numbers only!")
                continue
            elif n == 2:
                print("Please, input another even number")
                continue
            elif n == 0:
                print("Please, input another even number")
                continue
            break
        else:
            continue
        
    except ValueError:
        print("Invalid value entered!")

def prime_check(n):
    print("Number for checking is:", n, '\n')
    numbers = list(range(2, n + 1))
    for i in numbers:
        if i != 0:
            for k in range(2 * i, n + 1, i):
                numbers[k - 2] = 0

    primes = [x for x in numbers if x != 0]
    print("Prime numbers list:", primes, '\n')

    def task():
        for position in range(len(primes)):
            z = n - primes[position]
            if z in primes:
                print("The total amounts of these elements from prime number list give our value:", 2, "+",
                      primes[position])
            position += 1

    task()

if __name__ == '__main__':
    prime_check(n)

