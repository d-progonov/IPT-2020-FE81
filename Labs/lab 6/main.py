import functions as f

#test
#d1 = open("/Users/iced_flavour/Desktop/solution/data1.txt", "r")
#d2 = open("/Users/iced_flavour/Desktop/solution/data2.txt", "r")

#git
d1 = open("data1.txt", "r")
d2 = open("data2.txt", "r")

print("Lab 5.1", "\n")

try:
    N = int(d1.readline())
    an = []

    print("Enter non-negative numbers to sequence.")
    for i in range(0, N):
        i = int(d1.readline())
        an.append(i) 

    print("Your sequence is: ")
    print(an, "\n")

    print("Checking if some elements here is perfect square...")
    for i in range(0, N):
        print(an[i], "-", f.check_perfect_square(an[i]), end="; ")
    print("\n")

    segments = []; max_seg = [] 
    flow = False; a = 0            
    for i in range(0, N):
        check = f.check_perfect_square(an[i])
        if (check == True):
            segments.append(an[i])
            flow = True
        else:
            segments.append(0)
            flow = False
        
        if (flow == True):
            a = a + 1
        elif (flow == False):
            max_seg.append(a)
            a = 0
    max_seg.append(a)
    
    print("Max Segments are:", max_seg, "\n")
    max_s = max(max_seg)
    print("The largest segment with perfect squares is: ", max_s)
    print("\n")

    print("Lab 5.2", "\n")

    print("Enter a, c, m. They must be natural numbers (positive integers).")
    print("Otherwise - it will be converted using abs().")

    a = abs(int(d2.readline()))
    c = abs(int(d2.readline()))
    m = abs(int(d2.readline()))

    Res = f.f(m, a, c) 
    print("Result is: ", Res)

except f.Exception as non1:
    print(non1)

except ValueError:
    print("Entered elements must be non-negative!", "\n")
