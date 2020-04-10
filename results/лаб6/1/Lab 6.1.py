import primes
import os

from primes import read, write,prime_check

if __name__ == '__main__':
    inp = read()
    if len(inp) == 0:
        print("The file is empty!")
        exit()

while True:
    try:
        n = int(inp[0])
        if n % 2 != 0:
            print("Your value must be even and > 2! Choose another one, please")
            exit(0)
        elif n == 2:
            print("Iour value must be even and > 2! Choose another one, please")
            exit(0)
        break
    except ValueError:
        print("Invalid value entered!")
        exit(0)
part = prime_check(n)
write(part)

if os.stat("writing.txt").st_size != 0:
    print("The result is written to text file. Check it to get your result")
    
