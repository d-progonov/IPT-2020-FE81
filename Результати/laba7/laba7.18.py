alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']#,А, Б, В, Г, Д, Е, Ё, Ж, З, И, Й, К, Л, М, Н, О, П, Р, С, Т, У, Ф, Х, Ц, Ч, Ш, Щ, Ъ, Ы, Ь, Э, Ю, Я]
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

out1 = []
for ch in out:
    if ch == ' ':
        out1.append(' ')
        continue
    out1.append(alphabet[(alphabet.index(ch)-n)%26])
out1mess = ""
out1mess = out1mess.join(out1)

print("Decrypt: ",out1mess)
