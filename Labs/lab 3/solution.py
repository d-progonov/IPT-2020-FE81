
import math as mt

def part1():
    try:
        N = int(input("Number of elements: ")) 
        sum = 0
        n = 0
        while n < N: 
            curr = 1 / (9*(n**2) - 3*n - 2)
            print(n,"- element is: ", curr)
            sum = sum + curr
            n = n + 1
        print(float("{0:.4f}".format(sum)))

    except ValueError:
        print("\n", "Error: N could be only integer.")

# 2:

def part2():
    try:
        N = int(input("Number of elements: ")) 
        sum = 0
        n = 0
        for n in range(0, N):
            elem = pow(n, 2)*mt.exp(-mt.sqrt(n))
            print(n,"- element is: ", elem)
            sum = sum + elem
        print(float("{0:.4f}".format(sum)))
    
    except ValueError:
        print("\n", "Error: N could be only intege.")

part1()
part2()
