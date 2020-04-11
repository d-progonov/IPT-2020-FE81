def fib(index):
    if index < 0:
        raise IndexError()
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fib(index - 1) + fib(index - 2)


def fib_with_file(frm, to):
    with open(frm, "r") as frm_file:
        max_index = int(frm_file.readline())
    with open(to, "w") as to_file:
        for index in range(max_index):
            to_file.write(str(fib(index))+", ")
