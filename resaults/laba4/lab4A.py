import numpy

def in_n():
    try:
        n = int(input('Введите порядок n = '))
        if n <= 0 or n > 100:
            raise ValueError
        return n
    except ValueError:
        print('Неверный ввод')
        exit()

def linemake(curl, n):
    return numpy.hstack((numpy.arange(curl + 1, n + 1), numpy.zeros((curl))))

def matmake(n):
    res = numpy.arange(1, n + 1)
    curl = 1
    for x in range(1 ,n):
        nline = linemake(curl, n)
        res = numpy.vstack((res, nline))
        curl += 1
    return res

def main():
    n = in_n()
    print(matmake(n))

if __name__ == '__main__':
    main()


    

