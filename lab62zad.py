from math import isnan,isinf


def file_data():
    rez=[]
    try:
        f=open('input.txt')
    except FileNotFoundError:
        print("Error,file not find")
    while True:
        line = f.readline()
        if not line:
            break
        else:
            try:
                line=float(line)
            except ValueError:
                print("Number must be read")
                break
            if isnan(line):
                print("It must be a number")
                break
            if isinf(line):
                print("Number must be not inf")
                break
            if line<0:
                print("Number must be a positive")
                break
            if not line.is_integer():
                print("Number is not integer")
                break
            else:
                line = int(line)
            rez.append(line)
    f.close()
    return rez