#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    last_index = len(my_list) - 1
    copy_of_list = my_list.copy()

    if idx < 0 or idx > last_index:
        pass
    else:
        copy_of_list[idx] = element
    return copy_of_list
