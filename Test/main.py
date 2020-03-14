
N = 2
M = 4


def countdown(N, M):
    print('Starting')
    Temp = 1
    Res = 1
    while Temp <= M:
        yield Res
        Res += pow(N, Temp)
        Temp += 1


val = countdown(N, M)

print(next(val))
print(next(val))
print(next(val))
print(next(val))
