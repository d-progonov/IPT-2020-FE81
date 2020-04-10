import sys, os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from include.usefullFuncs import check_input_data


def lab7():
    print("HI! Lab7!")
    print("strs must be same len(exes will be ignored)")
    str1 = input("Input str1: ")
    str2 = input("Input str2: ")

    sp_str1 = list(str1)
    sp_str2 = list(str2)

    smaller_list_len = 0
    if len(sp_str1) <= len(sp_str2):
        smaller_list_len = len(sp_str1)
    else:
        smaller_list_len = len(sp_str2)

    no_mach_list = list()
    mach_list = list()
    for i in range(0, smaller_list_len, 1):
        if sp_str1[i] == sp_str2[i]:
            mach_list.append(sp_str1[i])
        else:
            no_mach_list.append(i)

    print("indexes that dont mach: ", no_mach_list)
    print("chars that mach: ", mach_list)


lab7()