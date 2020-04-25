from random import randrange


def is_even(num):
    return (num % 2) == 0


def main():
    randoms = [randrange(start=0, stop=90, step=1) for i in range(10)]
    print(randoms)
    k = int(input('Enter k(zero-indexed): '))
    randoms.pop(k)
    print(randoms)
    i = 0
    while i < len(randoms):
        if is_even(randoms[i]):
            randoms.insert(i + 1, 0)
            i += 1
        i += 1
    print(randoms)


if __name__ == '__main__':
    main()
