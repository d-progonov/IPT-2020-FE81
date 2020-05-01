import Lab5_2 as lab
file_i = open("Lab6_input.txt", "r")
file_o = open("Lab6_output.txt", "w")

try:
    s = file_i.readline()
    print(s)
    s = s.split()
    print(s)

    try:
        n = int(s[0])
        print("n = ", n)
        m = int(s[1])
        print("m = ", m)
        if n >= 0 and m >= 0:
            m = lab.A(n,m)
            print("Відповідь: ", m)
            file_o.write(str(m))
    except ValueError:
        print("Введіть невід'ємні числа")
        
except FileExistsError:
    print("Error")

file_i.close()
file_o.close()
