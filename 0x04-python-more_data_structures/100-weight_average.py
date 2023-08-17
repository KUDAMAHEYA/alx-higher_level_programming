#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    aver = 0
    wei = 0
    for tup in my_list:
        aver += tup[0] * tup[1]
        wei += tup[1]
    return float(aver / wei)
