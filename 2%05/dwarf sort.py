def gnome_sort(lst, size):
    i = 1
    while i < size:
        if (lst[i - 1] <= lst[i]):
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i-= 1
            if (i == 0):
                i = 1
    return lst

lists = list(map(int,input('Введите значения через пробел ').split()))

newlists = gnome_sort(lists, len(lists))
print(newlists)
