list1=[3,6,9,5,6,65,45]
list2=[5,8,6,3,6]
list3=[23, 56, 45]

def func(*lists):
    first = lists[0]
    for l in lists:
        if l == lists[0]:
            continue
        first = list(set(first) - set(l))
    print(first)

func(list1, list2, list3)
