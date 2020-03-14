def get_numbers():
    return input('Write numbers\n')


def res(nums):
    lst = [float(x) for x in nums.split(',') if bool(x) == True]
    tup = tuple(lst)
    return lst, tup

try:
    print(res(get_numbers()))
except ValueError:
    print('Bad input !')
    exit()
