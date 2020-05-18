import math

def progress(a0, step, n):
    if n == 1:
        return a0
    else:
        return a0 + (n - 1) * step + progress(a0, step, n - 1)

while True:
    try:
        A0 = input("Input the first element of your progression:")
        if A0 == "nan":
            print("Error! The first element can't be Not a number!")
            continue
        elif A0 == "inf":
            A0 = math.inf
        a0 = float(A0)
        break
    except ValueError:
        print("Invalid value entered!")


while True:
    try:
        Step = input("Input the step for your progression:")
        if Step == "nan":
            print("Error! The first element can't be Not a number!")
            continue
        elif Step == "inf":
            Step = math.inf
        step = float(Step)
        break
    except ValueError:
        print("Invalid value entered!")

while True:
    try:
        n = int(input("Input the number of elements for the progression:"))
        if n <= 0:
            print("Your progression can't exist if the number of progression elements is <= 0! Input another value, please")
            continue
        break
    except ValueError:
        print("Invalid value entered!")

if __name__ == '__main__':
    print(progress(a0, step, n))
