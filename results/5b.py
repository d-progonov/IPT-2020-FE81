def fib(index):
    if index < 0:
        raise IndexError()
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fib(index - 1) + fib(index - 2)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def max_len_of_prime(seq):
    max_len = 0
    cur_len = 0
    for i in seq:
        if is_prime(i):
            cur_len += 1
        else:
            if max_len < cur_len:
                max_len = cur_len
            cur_len = 0
    if max_len < cur_len:
        max_len = cur_len
    return max_len


def main():
    for i in range(15):
        print(fib(i), end=', ')
    print()
    print(max_len_of_prime([]))
    print(max_len_of_prime([2, 3, 5, 7, 11, 4, 2, 3, 5, 7, 11, 13]))
    print(max_len_of_prime([2, 3, 5, 7]))
    print(max_len_of_prime([4, 4, 4, 4, 2, 3, 5, 7]))


if __name__ == '__main__':
    main()
