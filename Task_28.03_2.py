alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']#, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, ]
messlist = []
while (1):
    try:
        mess = str(input("message: "))
        break
    except ValueError:
        print("Cannot read")
while (1):
    try:
        n = int(input("+n: "))
        if n<0:
            raise ValueError
        break
    except ValueError:
        print("Cannot read: ")

for ch in mess:
    messlist.append(ch)
out = []
for ch in messlist:
    if ch == ' ':
        out.append(' ')
        continue
    out.append(alphabet[(alphabet.index(ch)+n)%26])
outmess = ""
outmess = outmess.join(out)
print("Crypted: ",outmess)

out2 = []
for ch in out:
    if ch == ' ':
        out2.append(' ')
        continue
    out2.append(alphabet[(alphabet.index(ch)-n)%26])
out2mess = ""
out2mess = out2mess.join(out2)
print("Decrypt: ",out2mess)