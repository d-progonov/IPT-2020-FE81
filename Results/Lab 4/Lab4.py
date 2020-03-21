import sys, os, math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from include.usefullFuncs import check_input_data


def lab4():
    print("HI! Lab4!")
    x = input("Input x: ")

    result = check_input_data(1.1, x)


print(lab4())