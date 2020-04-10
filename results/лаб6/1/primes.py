def read():
    try:
        file = open('reading.txt', 'r')
    except FileNotFoundError:
        print("File is not found! Check whether it is in the same directory with your project")
        exit()

    inp = [line.strip() for line in file]
    file.close()
    return inp

def write(part):
    file = open('writing.txt', 'w') 
    file.write(part)
    file.close()
    return True

def prime_check(n):
    numbers = list(range(2, n + 1))
    for i in numbers:
        if i != 0:
            for k in range(2 * i, n + 1, i):
                numbers[k - 2] = 0

    primes = [x for x in numbers if x != 0]

    final = []

    for position in range(len(primes)):
        z = n - primes[position]
        if 2 in primes:
            final.append("'l'he pair of these elements from prime number list give our value in sum:")
            final.append(z)
            final.append("+")
            final.append(primes[position])
            final.append('\n')
        position += 1
    strl = ''.join(str(e) for e in final)
    return (strl)
