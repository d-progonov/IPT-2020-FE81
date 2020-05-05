import sys, os, math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from include.usefullFuncs import check_input_data

from collections import Counter

WordCountMap = dict()


def alph_sort(outList, words_to_sort):
    i = words_to_sort
    resultList = []
    while i > 0:
        tmp = []
        for word in outList:
            if i == WordCountMap[word]:
                tmp.append(word)

        if len(tmp) == 0:
            i -= 1
            continue
        tmp.sort()
        resultList += tmp
        i -= 1

    return resultList


def lab10():
    print("HI! Lab10!")
    num = input("Input how many words to sort: ")

    words_to_sort = check_input_data(1, num)
    if not words_to_sort:
        return "Wrong input!!!"
    inputList = []
    for i in range(0, words_to_sort):
        inputList.append(input("Word: "))

    for i in inputList:
        if WordCountMap.__contains__(i):
            WordCountMap[i] += 1
        else:
            WordCountMap[i] = 1

    outList = [key for key, value in Counter(inputList).most_common()]

    resultList = alph_sort(outList, words_to_sort)

    print("The list after sorting: ")
    for i in resultList:
        number = WordCountMap[i]
        print((i + ", ") * number, end="")


print(lab10())
