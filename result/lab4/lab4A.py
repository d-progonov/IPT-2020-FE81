import numpy

def get_n():
    try:
        n = int(input('n = '))
        if n <= 0 or n > 1000:
            raise ValueError
        return n
    except ValueError:
        print('Bad input')
        exit()

def create_line(curr_line, n):
    return numpy.hstack((numpy.arange(curr_line + 1, n + 1), numpy.zeros((curr_line))))

def create_matrix(n):
    result = numpy.arange(1, n + 1)
    curr_line = 1
    for x in range(1 ,n):
        n_line = create_line(curr_line, n)
        result = numpy.vstack((result, n_line))
        curr_line += 1
    return result
m = create_matrix(15)


def main():
    n = get_n()
    print(create_matrix(n))


    
if __name__ == '__main__':
    main()
