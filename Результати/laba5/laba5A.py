while True:
    try:
        n = int(input("Input any natural number for checking:"))
        if n <= 0:
            print("Natural numbers only excepted! input another value, please")
            continue
        break
    except ValueError:
        print("Invalid value entered!")
        

def prime_check(n):
    print("Number for checking is:", n, '\n')
    numbers = list(range(2, 2 * n + 1))
    for i in numbers:
        if i != 0:
            for k in range(2 * i, 2 * n + 1, i):
                numbers[k - 2] = 0
    
    primes = [x for x in numbers if x != 0]
    taken = list(filter(lambda x: 2 * n >= x >= n, primes))
    
    print("Prime numbers list:", primes, '\n')
    print ("The range of searching of twin numbers:", taken, '\n')
    
    result = []
    
    def task():
        for i in range(len(taken) - 1):
            if taken[i] == taken[i + 1] - 2:
                result.append("The pair of twins:")
                result.append(taken[i])
                result.append("and")
                result.append(taken[i + 1])
                result.append('\n')
    
    if len(result) == 0:
        print("There are no twin numbers!")
    
    task()

if __name__ == '__main__':
    prime_check(n)
