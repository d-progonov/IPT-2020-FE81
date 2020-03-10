def get_message(file = ''):
    if len(file) == 0:
        return input('Write string to encrypt:\n')
    else:
        try:
            msg_file = open(file,'r')
        except FileNotFoundError:
            print('Can not to open file')
        msg = msg_file.read()
        msg_file.close()
        return msg


def encrypt(msg):
    result = str()
    result += msg[0]
    for i in range(1,len(msg)):
        if int(msg[i]) - 1 == int(msg[i]):
            result += '1'
        else:
            result += '0'
    return result
