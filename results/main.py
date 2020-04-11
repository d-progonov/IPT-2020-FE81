from fib import *
from max_len_of_prime import *


def main():
    fib_with_file("fib_input.txt", "fib_out.txt")
    max_len_of_prime_with_file("primes_input.txt", "primes_out.txt")


if __name__ == '__main__':
    main()
