def get_input():
    inpt = input('Write number to check or Enter to exit:\n')
    if len(inpt) == 0:
        exit()
    else:
        try:
            num = int(inpt)
            if num < 1 or num >= 1e+12:
                raise ValueError
            return num
        except ValueError:
            print('Bad number !')
            return False


class PrimesFinder:
    def __init__(self):
        self.initial_primes_list = self.create_primes_list(int(1e+3), list(range(2, int(1e+6))))

    def create_primes_list(self, sqrt_num_, lst, pos = 0):
        if lst[pos] > sqrt_num_:
            return lst
        else:
            lst = list(x for x in lst if (x % lst[pos] != 0 or x == lst[pos]))
            return self.create_primes_list(sqrt_num_, lst, pos + 1)

    def is_prime(self, num):
        if num < 1e+6:
            return (num in self.initial_primes_list)

        check_to = num ** (1/2)
        for i in range(0, len(self.initial_primes_list)):
            if self.initial_primes_list[i] > check_to:
                return True
            if num % self.initial_primes_list[i] == 0 and num != self.initial_primes_list[i]:
                return False
        return -1


def main():
    print('Initialization...')
    f = PrimesFinder()
    num = get_input()
    while True:
        if bool(num):
            is_p = f.is_prime(num)
            if is_p:
                print('Number {} IS prime'.format(num))
            else:
                print('Number {} is NOT prime'.format(num))
        num = get_input()


main()
