n = input()
ans = True
def is_digit(t):
    if t.isdigit():
       return True
    else:        
        try:
            int(t)
            return True
        except ValueError:
            print(t,"not an intager")
            return False
if is_digit(n):
    n = int(n)
    if n >= 2:
        my_list = [2]
        for i in range(2, n+1):
            for j in range(0, len(my_list)):
                if i%my_list[j] == 0:
                    ans = False
                    break
            if ans == True:
                my_list.append(i)
            else: ans = True
        print("Prime numbers:")
        for k in range(0, len(my_list)):
            print(my_list[k], end = " ")
    else: print("The number must be greater than 2 (>=2)")
else: print("Please use numbers (>= 2)")
                



