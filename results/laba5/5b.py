def fib(index):
    if index < 0:
        raise IndexError()
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fib(index - 1) + fib(index - 2)
