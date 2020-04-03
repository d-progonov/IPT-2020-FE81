def g(n, a, c):
    res = (a * (n + c)) % 10
    return res


def f(n, *args):
    a = args[0]
    c = args[1]
    if n >= 0 and n <= 9:
        res = n
        return res
    else:
        res2 = g(n, a, c) * f(n - 1 - g(n, a, c), a, c) + n
        return res2
