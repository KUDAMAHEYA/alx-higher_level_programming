#!/usr/bin/python3
def mk_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        mk = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > mk:
                mk = my_list[i]
        return mk
