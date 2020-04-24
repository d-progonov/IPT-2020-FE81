def get_message():
    msg = input('Write string to encrypt:\n')
    if len(msg.replace('1','').replace('0','')) == 0 or len(msg.replace('-','').replace('.','')) == 0:
        return msg
    else:
        print('Bad string !')
        exit()


def is_nums(msg):
    return msg.count('0') != 0 or msg.count('1') != 0

def convert(msg):
    if is_nums(msg):
        msg = msg.replace('0', '.').replace('1', '-')
    else:
        msg = msg.replace('.', '0').replace('-', '1')
    return msg

def encrypt(msg):
    need_to_convert = False
    if not is_nums(msg):
        msg = convert(msg)
        need_to_convert = True
    res_msg = msg[:1]
    for i in range(1, len(msg)):
        if msg[i - 1] == msg[i]:
            res_msg += '1'
        else:
            res_msg += '0'
    if need_to_convert:
        return convert(res_msg)
    return res_msg

def decrypt(msg):
    need_to_convert = False
    if not is_nums(msg):
        msg = convert(msg)
        need_to_convert = True
    res_msg = msg[:1]
    not_ = lambda x: '1' if x == '0' else '0'
    for i in range(1, len(msg)):
        res_prev = res_msg[i - 1]
        if msg[i] == '1':
            res_msg += res_prev
        else:
            res_msg += not_(res_prev)
    if need_to_convert:
        return convert(res_msg)
    return res_msg

def main():
    msg = get_message()
    e_msg = encrypt(msg)
    d_msg = decrypt(e_msg)
    print('{} -> {} -> {}'.format(msg, e_msg, d_msg))
main()
