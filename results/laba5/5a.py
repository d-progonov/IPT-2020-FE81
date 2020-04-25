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
