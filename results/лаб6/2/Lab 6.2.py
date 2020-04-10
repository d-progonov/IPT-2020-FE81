
from module import read,write,fast,value,power
import os

if __name__ == "__main__":
    inp = read()
    if len(inp) == 0:
        print("The file is empty!")
        exit(0)

    inpVal = str(inp[0])
    if not value(inpVal):
        exit()
    my_value = value(inpVal)
    print("Your value for checking is:", my_value)

    inpPow = str(inp[0])
    if not power(inpPow):
        exit()
    my_power = power(inpPow)
    print("The power of your value is:", my_power)

    result = fast(my_value, my_power)
    strl = str(result)
    write(strl)

if os.stat("writing.txt").st_size != 0:
    print("The result is written to text file. Cheek it to get your result")

