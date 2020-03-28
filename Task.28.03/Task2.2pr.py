def encryptCaesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind+shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind+shift]
        else:
            ret += x
    return ret
 
def decryptCaesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind-shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind-shift]
        else:
            ret += x
    return ret
