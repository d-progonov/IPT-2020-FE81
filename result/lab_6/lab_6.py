from functions import f
from sys import exit

while (True):
    try:
        file = open("task.txt", 'r')
    except Exception:
        input('Wrong data. Press any key to exit...')
        continue
    break
while (True):
    try:
        s = float(file.readline())
    except ValueError:
        input('Wrong data type of s. Press any key to exit...')
        continue
    break
while (True):
    try:
        t = float(file.readline())
    except ValueError:
        input('Wrong data type of t. Press any key to exit...')
        continue
    break
file.close()

endfile=open("results.txt", 'w')

endfile.writelines("Result={:.4f}".format(f(t, -2*s, 1.17)-f(2.2, t, s-t)))

endfile.close()
