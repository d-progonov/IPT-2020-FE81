def triple_decode(msg):
    if len(msg)%3 != 0:
        return "Bad encoding"
    out = []
    for i in range(0, len(msg), 3):
        sum = 0
        for j in range(3):
            sum += int(msg[i+j])
        out.append(0 if sum<2 else 1)
    return out
    
out = triple_decode(input("Enter message: "))
print("Decoded message: ", end='')
print(out)
input()
