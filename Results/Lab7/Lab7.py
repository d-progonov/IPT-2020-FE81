
def hex_num(num):
    t = hex(num).replace("0x", "")
    return t.upper()
    
def bin_num(num):
    return bin(num).replace("0b", "")

if __name__ == '__main__':
    strn = input("Enter string const: ")
    answ = []
    summ = 0
    strn = strn.upper()
    for i in range(len(strn)):
        answ.append(ord(strn[i]))

    for i in answ:
        summ += i
    
    hexAnsw = hex_num(summ)
    binAnsw = bin_num(summ)
    
    print("Answer (hexadecimal value): ", hexAnsw)
    print("Answer (decimal value): ", summ)
    print("Answer (binary value): ", binAnsw)
