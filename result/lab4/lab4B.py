import numpy
from lab4A import get_n
def get_():
    try:
        a = int(input())
        if a < 1 or a > 100:
            raise ValueError
        else:
            return a
    except ValueError:
        print('Bad input')
        exit()


class Ring:
    def __init__(self, arr_size = 4):
        self.arr = numpy.arange(1, arr_size + 1)
        self.arr_size  = arr_size
        self.cur_pos = 0
    def go_right(self):
        if self.cur_pos < self.arr_size - 1:
            self.cur_pos += 1
        else:
            self.cur_pos = 0

    def go_left(self):
        if self.cur_pos > 0:
            self.cur_pos -= 1
        else:
            self.cur_pos = self.arr_size - 1

    def add_el(self, el):
        self.arr = numpy.hstack((self.arr, el))
        self.arr_size += 1

    def print(self, dir, from_pos):
        if from_pos > self.arr_size:
            print('Bad index of element')
            exit()
        self.cur_pos = from_pos - 1
        for i in range(0, self.arr_size + 2):
            print(self.arr[self.cur_pos], end = ' ')
            if dir == 'left':
                self.go_left()
            else:
                self.go_right()
        print()


def main():
    print('Number of elements = ', end = '')
    size = get_()
    print('Start printing from: ', end = '')
    start_index = get_()
    my_ring = Ring(size)
    print('Left->', end = '')
    my_ring.print('left', start_index)
    print('Added elemnts {}, {}'.format(my_ring.arr[0],  my_ring.arr[-1]))
    my_ring.add_el(my_ring.arr[0])
    my_ring.add_el(my_ring.arr[-2])
    print('Right->', end = '')
    my_ring.print('right', start_index)

main()
