
N = 3
M = 4

def countdown(N, M):
    print('Starting')
    Temp = 0
    Res = 1
    while Temp < M:
        yield Res
        Res =+ pow(N, M)


val = countdown(N, M)

print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))