
try:
    print("Input string constant. Use ' ' to split HEX constants.")
    print("Example: 0x2 0x3 0x4")
    string = str(input("String: "))
    print("\n")

    newstring = string.split('0x')
    newstring = newstring[1:]

    hex_mull = 1

    for i in range(0, len(newstring)):
        newstring[i] = str.upper(newstring[i])
        newstring[i] = '0x' + newstring[i]
        hex_elem = int(newstring[i], 16);  print("Hex element (int-object): ", hex_elem)
        hex_mull = hex_mull * hex_elem

    if (len(newstring) == 0): hex_mull = 0; print("No HEX numbers found.", "\n")
    hex_mull = hex(hex_mull) 

    print("All elements as HEX: ", newstring)
    print("Hex mull: ", hex_mull, "\n")

    dec_array = []
    for i in range(0, len(newstring)):
        hex_elem = str(int(newstring[i], 16))  
        dec_elem = int(hex_elem, 10)
        print("Dec element (int-object): ", dec_elem)
        dec_array.append(dec_elem)

    hex_mull = str(int(hex_mull, 16))  
    dec_mull = int(hex_mull, 10)

    print("All elements as DEC: ", dec_array)
    print("Dec mull is: ", dec_mull)

except ValueError:
    print("Can not convert to HEX!")
    print("Use sixteen distinct symbols '0'–'9' to represent values zero to nine, and 'A'–'F' to represent values ten to fifteen.")

