import euclidean

while(1):
    try:
        filename = str (input("Enter file name: "))
        file = open(filename, 'r')
    except Exception:
        print("Unable to find given path.")
        continue
    try:
        pre = str (file.readline())
        n = int (pre)
        1/(n+abs(n))
    except Exception:
        print("{} is wrong data type for variable n (must be natural int).".format(pre))
        continue
    try:
        pre = str (file.readline())
        m = int (pre)
        1/(m+abs(m))
    except Exception:
        print("{} is wrong data type for variable m (must be natural int).".format(pre))
        continue
    break
file.close()

file = open('result_gcd.txt', 'w')
result = "Greatest common divisor of "+str(n)+" and "+str(m)+" is "+str(euclidean.gcd(n,m))+"."
file.writelines(result)
print("Result has been written to result_gcd.txt")
file.close()
input("Any key to exit...")