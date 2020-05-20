import random

def str_f(string):
    newstring = string[1:-1]
    return newstring

try: 
    A = int(input("Enter matrix order: " ))
    print("Choose method, what you want to fill matrix.")
    print("     1 - simple iteration fill from 0 to A.")
    print("     2 - random default fill from -5 to 5.")
    print("     3 - keyboard-fill.")
    k = int(input("Choose input method: " ))

    if (k == 1):
        Arr = [[ i for i in range(0, A)] for j in range(0, A)] 
    
    if (k == 2):
        Arr = [[ random.randint(-5, 5) for i in range(0, A)] for j in range(0, A)] 

    if (k == 3):
        Arr = [[ int(input("elem is: ")) for i in range(0, A)] for j in range(0, A)]

    else:
        print("Default random fill.")
        Arr = [[ random.randint(-5, 5) for i in range(0, A)] for j in range(0, A)]
        
    # Printing elements: 
    for elem in Arr:
        print(elem)
    print("\n")

    b = []

    for i in range(0, A):
        temp_str = str(Arr[i])
        temp_str = str_f(temp_str)

        Arr[i].sort(reverse=False);  LtoH_sorted = str(Arr[i])   # 1, 2, 3, 4, 5 
        Arr[i].sort(reverse=True);   HtoL_sorted = str(Arr[i])   # 5, 4, 3, 2, 1

        newLtoH = str_f(LtoH_sorted)
        newHtoL = str_f(HtoL_sorted)

        print("Temp string: ", temp_str)
        print("From low to  high sort: ", newLtoH, "Len: ", len(newLtoH))
        print("From high to low sort: ",  newHtoL, "Len: ", len(newHtoL), "\n")

        if (temp_str == newLtoH):     # low -> high
            b.append(1)
        elif (temp_str == newHtoL):   # high -> low
            b.append(1)
        else:
            b.append(0)

    print("b-array is: ", b)

except ValueError:
    print("Inpur Error!")