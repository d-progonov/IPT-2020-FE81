print("Lab 5.1", "\n")

class Exception(Exception):
    def init(self, text):
        self.txt = text

def check_perfect_square(a):
    if (a == 1):
        print("Processing Error!")
        raise Exception("The 'a' must not equal to 1!")

    x = a // 2                  
                                 
    seen = set([x])              
    while x * x != a:            
        x = (x + (a // x)) // 2  
        if x in seen: 
            return False
        seen.add(x)        
                                 
    return True

try:
    N = int(input("Enter N: "))
    an = []

    print("Enter non-negative numbers to sequence.")
    for i in range(0, N):
        i = int(input("Elem is:" ))
        an.append(i)

    print("Your sequence is: ")
    print(an, "\n")

    print("Checking if some elements here is perfect square...")
    for i in range(0, N):
        print(an[i], "-", check_perfect_square(an[i]), end="; ")
    print("\n")

    segments = []; max_seg = [] 
    flow = False; a = 0            
    for i in range(0, N):
        check = check_perfect_square(an[i])
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

except Exception as non1:
    print(non1)

except ValueError:
    print("Entered elements must be non-negative!")


print("Lab 5.2", "\n")

print("Enter a, c, m. They must be natural numbers (positive integers).")
print("Otherwise - it will be converted using abs().")

a = abs(int(input("Enter a: " )))
c = abs(int(input("Enter c: " )))
m = abs(int(input("Enter m: " )))

def f(n):
    if (0 <= n <= 9):
        return n
    else:
        res = g(n) * f(n-1-g(n)) + n
        return res

def g(n):
    res = (a*n + a*c) % 10
    return res

Res = f(m)
print("Result is: ", Res)
