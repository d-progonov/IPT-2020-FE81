from utils import is_prime


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


def max_len_of_prime_with_file(frm, to):
    with open(frm, "r") as frm_file:
        seq = [int(x) for x in frm_file]
    with open(to, "w") as to_file:
        to_file.write(str(max_len_of_prime(seq)))
