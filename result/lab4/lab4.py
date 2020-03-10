from lab2 import num_sign
import numpy

################################################
#              Part A
###############################################
def create_array(n: int):
    temp = list(range(1,n+1))
    str_for_arr = list()
    for i in range(0,n):
        str_for_arr.append(temp)
    return numpy.array(str_for_arr)

def fill_zero(array, size, str, num_of_elements):  #str - idex of string to convert
    for i in range(0,num_of_elements):
        array[str,size - i - 1] = 0

def add_necessary_part(array, size, str):
    for i in range(0, size - str):
        array[str,i] += str

def spec_convert(array, n):
    current_str = 0
    for i in range(0, n):
        fill_zero(array,n,current_str,current_str)
        add_necessary_part(array,n,current_str)
        current_str += 1
    return array

def valid_n(n: str):
    try:
        int(n)
    except ValueError:
        print('Bad input!')
        exit()
    if int(n) > 3000:
        print('Num is too big, cant works with it')
        exit()
    if num_sign(int(n)) != 1 or type(n) == float():
        print('Size of array cant be negative or 0!')
        exit()
    return True
################################################
#              Part B
###############################################
class Ring(object):
    def __init__(self, size):
        self.size = size
        self.arr = numpy.array(list(range(0,size)))
        self.current_pos = 0
    def step_forward(self):
        if self.current_pos >= (self.size - 1):
            self.current_pos = 0
        else:
            self.current_pos += 1
    def step_back(self):
        if (self.current_pos - 1) < 0:
            self.current_pos = self.size - 1
        else:
            self.current_pos -= 1
    def print_ring(self, num_of_el, from_pos, mod): # mod - left/right; from_pos - index to start from
        save_pos = self.current_pos
        self.current_pos = from_pos
        string_to_print = str()
        for i in range(0,num_of_el):
            string_to_print += str(self.arr[self.current_pos]) + ' '
            if mod == 'left':
                self.step_back()
            else:
                self.step_forward()
        self.current_pos = save_pos
        print(string_to_print)
    def push(self, val):
        self.arr = self.arr.tolist()
        self.arr.append(val)
        self.arr = numpy.array(self.arr)
        self.size += 1






def main():
    n = input('Size of array = ')
    print("###########\nPart A\n###########")
    if valid_n(n) == True:
        n = int(n)
        arr = spec_convert(create_array(n),n)
        if n < 15:
            print(arr)
        else:
            print('Array is too big, cant prints it')
    print("###########\nPart B\n###########")
    myring = Ring(n)
    print('Ring <- :')
    myring.print_ring(myring.size + 1, 0, 'left')
    myring.push(myring.arr[0])
    myring.push(myring.arr[-2])  # arr[-1] now it is arr[0]
    print('Ring -> :')
    myring.print_ring(myring.size + 1, 0, 'right')

if __name__ == '__main__':
    main()
