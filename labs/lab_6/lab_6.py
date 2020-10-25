import lab_5b as l5b
from in_out_module import *

def main():
    try:
        a, b, c = open_file()
        num = l5b.geom_progression(a, b, c)
        write_file(num)
    except TypeError:
        print("End of program")
            

if __name__ == "__main__":
    main()  