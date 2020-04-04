import lab5
from get_data import get_data
from save_result import save_result

def main():
    primes = lab5.get_primes(1000000)
    n = get_data()
    if lab5.valid_n(n) == True:
        n = int(n)
        a,b = lab5.get_answer(n, primes)
        save_result('True:\n{} + {} = {}'.format(a, b, n))


if __name__ == '__main__':
    main()
